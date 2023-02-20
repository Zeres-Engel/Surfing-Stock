import os
import numpy as np
import pandas as pd
import datetime as dt

#API
import vnstock
from vnstock import *

import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
class Functions:
    def __init__(self):
        model = Sequential()
        cells = 248
        model.add(LSTM(units = cells, activation='tanh', recurrent_activation='sigmoid', input_shape = (7, 31))) #input traning date and predicting date 
        model.add(Dropout(0.1))
        model.add(Dense(units = 1))  
        self.model = model
        
    def set_svg_icon(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "./gui/images/svg_icons/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon
    def set_svg_image(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "./gui/images/svg_images/"
        path = os.path.join(app_path, folder)
        image = os.path.normpath(os.path.join(path, icon_name))
        return image
    def set_image(image_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "./gui/images/images/"
        path = os.path.join(app_path, folder)
        image = os.path.normpath(os.path.join(path, image_name))
        return image
    def Crawler():
        fhandle = open("./gui/data/companylist.txt","r")
        for line in fhandle.readlines():
            company = line.strip()
            start = "2000-02-15" 
            end = today = dt.datetime.now().strftime("%Y-%m-%d") 
            df = vnstock.stock_historical_data(symbol = company, start_date = start, end_date = end)
            df.to_csv(f"./gui/data/raw/{company}.csv",encoding = "utf-8")
    def Preprocessing():
        fhandle = open("./gui/data/companylist.txt","r")
        for line in fhandle.readlines():
            company = line.strip()
            df = pd.read_csv(f"./gui/data/raw/{company}.csv", delimiter = ",", encoding="utf-8")
            df['H-L'] = df['High'] - df['Low']
            df['O-C'] = df['Open'] - df['Close']
            MA1 = 7
            MA2 = 14
            MA3 = 21
            MA4 = 28
            df['AR'] = df['H-L']/df['O-C']
            df[f'ME_{MA1}'] = df['Close'].rolling(window = MA1).median()
            df[f'ME_{MA2}'] = df['Close'].rolling(window = MA2).median()
            df[f'ME_{MA3}'] = df['Close'].rolling(window = MA3).median()
            df[f'ME_{MA4}'] = df['Close'].rolling(window = MA4).median()
            df[f'RANK_{MA1}'] = df['Close'].rolling(window = MA1).rank()
            df[f'RANK_{MA2}'] = df['Close'].rolling(window = MA2).rank()
            df[f'RANK_{MA3}'] = df['Close'].rolling(window = MA3).rank()
            df[f'RANK_{MA4}'] = df['Close'].rolling(window = MA4).rank()
            df[f'VAR_{MA1}'] = df['Close'].rolling(window = MA1).var()
            df[f'VAR_{MA2}'] = df['Close'].rolling(window = MA2).var()
            df[f'VAR_{MA3}'] = df['Close'].rolling(window = MA3).var()
            df[f'VAR_{MA4}'] = df['Close'].rolling(window = MA4).var()
            df[f'SMA_{MA1}'] = df['Close'].rolling(window = MA1).mean()
            df[f'SMA_{MA2}'] = df['Close'].rolling(window = MA2).mean()
            df[f'SMA_{MA3}'] = df['Close'].rolling(window = MA3).mean()
            df[f'SMA_{MA4}'] = df['Close'].rolling(window = MA4).mean()
            df[f'SD_{MA1}'] = df['Close'].rolling(window = MA1).std()
            df[f'SD_{MA2}'] = df['Close'].rolling(window = MA2).std()
            df[f'SD_{MA3}'] = df['Close'].rolling(window = MA3).std()
            df[f'SD_{MA4}'] = df['Close'].rolling(window = MA4).std()
            df[f'Ske_{MA1}'] = df['Close'].rolling(window = MA1).skew()
            df[f'Ske_{MA2}'] = df['Close'].rolling(window = MA2).skew()
            df[f'Ske_{MA3}'] = df['Close'].rolling(window = MA3).skew()
            df[f'Ske_{MA4}'] = df['Close'].rolling(window = MA4).skew()
            df[f'Kur_{MA1}'] = df['Close'].rolling(window = MA1).kurt()
            df[f'Kur_{MA2}'] = df['Close'].rolling(window = MA2).kurt()
            df[f'Kur_{MA3}'] = df['Close'].rolling(window = MA3).kurt()
            df[f'Kur_{MA4}'] = df['Close'].rolling(window = MA4).kurt()
            df[df.replace([np.inf, -np.inf], np.nan).notnull().all(axis = 1)]
            df.dropna(inplace = True)
            df.to_csv(f"./gui/data/prepaired/{company}pre.csv", encoding = "utf-8")
        
    def SetLineGraph(self,company):
        df = pd.read_csv(f"./gui/data/prepaired/{company}pre.csv", encoding = "utf-8")
        MA1 = 7
        MA2 = 14
        MA3 = 21
        MA4 = 28
        scaler_x = MinMaxScaler(feature_range = (0, 1))
        scaler_y = MinMaxScaler(feature_range = (0, 1))
        cols_x = ['H-L', 'O-C', 'Volume', f'ME_{MA1}', f'ME_{MA2}', f'ME_{MA3}', f'ME_{MA4}', f'VAR_{MA1}', f'VAR_{MA2}', f'VAR_{MA3}', f'VAR_{MA4}', f'RANK_{MA1}', f'RANK_{MA2}', f'RANK_{MA3}', f'RANK_{MA4}', f'SMA_{MA1}', f'SMA_{MA2}', f'SMA_{MA3}', f'SMA_{MA4}', f'SD_{MA1}' ,f'SD_{MA2}', f'SD_{MA3}', f'SD_{MA4}', f'Ske_{MA1}', f'Ske_{MA2}', f'Ske_{MA3}', f'Ske_{MA4}', f'Kur_{MA1}', f'Kur_{MA2}', f'Kur_{MA3}', f'Kur_{MA4}'] #Variables for training
        cols_y = ['Close']
        scaled_data_x = scaler_x.fit_transform(df[cols_x].values.reshape(-1, len(cols_x))) 
        scaled_data_y = scaler_y.fit_transform(df[cols_y].values.reshape(-1, len(cols_y)))
        self.model = load_model(f"./gui/model/{company}.h5")
        real_prices = df.loc[len(df)-7:, ['Close', 'Volume']]
        real_prices = np.array(real_prices)
        predict_prices = real_prices[:, 0]
        x_predict = df[len(df)-7:][cols_x].values.reshape(-1, len(cols_x))
        x_predict = scaler_x.transform(x_predict)
        x_predict = np.array(x_predict)
        x_predict = x_predict.reshape(1, x_predict.shape[0], len(cols_x))
        prediction = self.model.predict(x_predict)
        prediction = scaler_y.inverse_transform(prediction)
        predict_prices = np.append(predict_prices, prediction)
        font = "Segoe UI"  
        font_color = "gray"  
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.grid(True, linewidth=0.5, color='gray', zorder=1)
        if predict_prices[6] < predict_prices[7]:
            ax.plot(predict_prices, color="#58D68D", label=f"predict", zorder=2)
        else:
            ax.plot(predict_prices, color="#FF6666", label=f"predict", zorder=2)
        ax.plot(real_prices[:, 0], color="#FFCC33", label=f"real", zorder=2)
        real_volumes = np.multiply(real_prices[:, 1], (np.max(predict_prices)/2/(np.max(real_prices[:, 1]))))
        x = np.arange(len(real_volumes))  
        width = 0.4  
        ax.bar(x - width/2, real_volumes , width, color="#33CCFF", label='volume', align='edge', zorder=2)
        ax.scatter(np.arange(len(real_prices[:, 0])), real_prices[:, 0], color='#FFCC33', zorder=2)
        for i, price in enumerate(real_prices[:, 0]):
            ax.annotate(f"{price:.2f}", (i, real_prices[i, 0]), xytext=(5, 10), textcoords='offset points', color='#FFCC33', ha='center', zorder=2)
        if predict_prices[6] < predict_prices[7]:
            ax.scatter(len(predict_prices)-1, predict_prices[-1], color="#58D68D", zorder=2)
            ax.annotate(predict_prices[-1], xy=(len(predict_prices)-1, predict_prices[-1]), xytext=(-10, 10), textcoords='offset points', color="#58D68D",zorder=2 )
        else:
            ax.scatter(len(predict_prices)-1, predict_prices[-1], color="#FF6666", zorder=2)
            ax.annotate(predict_prices[-1], xy=(len(predict_prices)-1, predict_prices[-1]), xytext=(-10, 10), textcoords='offset points', color="#FF6666", zorder=2)
        ax.legend(loc= 'lower right')
        ax.spines['bottom'].set_color('#6699FF')
        ax.spines['left'].set_color('#6699FF')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(colors=font_color)
        ax.set_ylim(0, np.max(predict_prices)*1.2)
        plt.savefig(f"./gui/images/svg_images/{company}.svg", format="svg", transparent=True)
    
    def Evaluation(self, company):
        df = pd.read_csv(f"./gui/data/prepaired/{company}pre.csv", encoding = "utf-8")
        MA1 = 7
        MA2 = 14
        MA3 = 21
        MA4 = 28
        scaler_x = MinMaxScaler(feature_range = (0, 1))
        scaler_y = MinMaxScaler(feature_range = (0, 1))
        cols_x = ['H-L', 'O-C', 'Volume', f'ME_{MA1}', f'ME_{MA2}', f'ME_{MA3}', f'ME_{MA4}', f'VAR_{MA1}', f'VAR_{MA2}', f'VAR_{MA3}', f'VAR_{MA4}', f'RANK_{MA1}', f'RANK_{MA2}', f'RANK_{MA3}', f'RANK_{MA4}', f'SMA_{MA1}', f'SMA_{MA2}', f'SMA_{MA3}', f'SMA_{MA4}', f'SD_{MA1}' ,f'SD_{MA2}', f'SD_{MA3}', f'SD_{MA4}', f'Ske_{MA1}', f'Ske_{MA2}', f'Ske_{MA3}', f'Ske_{MA4}', f'Kur_{MA1}', f'Kur_{MA2}', f'Kur_{MA3}', f'Kur_{MA4}'] #Variables for training
        cols_y = ['Close']
        scaled_data_x = scaler_x.fit_transform(df[cols_x].values.reshape(-1, len(cols_x))) 
        scaled_data_y = scaler_y.fit_transform(df[cols_y].values.reshape(-1, len(cols_y)))
        pre_day = 7
        x_total = [] # Variables today
        y_total = [] #Close price tomorrow
        for i in range(pre_day, len(df)):
            x_total.append(scaled_data_x[i - pre_day : i])
            y_total.append(scaled_data_y[i])
        test_size = 365
        x_train = np.array(x_total[:len(x_total)-test_size]) 
        y_train = np.array(y_total[:len(y_total)-test_size])
        x_test = np.array(x_total[len(x_total)-test_size:]) 
        y_test = np.array(y_total[len(y_total)-test_size:]) 
        real_prices = df.loc[len(df)-test_size:, ['Close', 'Volume']]
        real_prices = np.array(real_prices)
        predict_prices = self.model.predict(x_test)
        predict_prices = scaler_y.inverse_transform(predict_prices)
        font = "Segoe UI"  
        font_color = "gray"  
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.grid(True, linewidth=0.5, color='gray', zorder=1)
        ax.plot(real_prices[:, 0], color="#FFCC33", label=f"real", zorder=2)
        ax.plot(predict_prices, color="#58D68D", label=f"predict", zorder=2)
        real_volumes = np.multiply(real_prices[:, 1], (np.max(predict_prices)/2/(np.max(real_prices[:, 1]))))
        x = np.arange(len(real_volumes))  
        width = 0.4  
        ax.bar(x - width/2, real_volumes , width, color="#33CCFF", label='volume', align='edge', zorder=2)
        ax.legend(loc= 'lower right')
        ax.spines['bottom'].set_color('#6699FF')
        ax.spines['left'].set_color('#6699FF')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(colors=font_color)
        ax.set_ylim(0, max(np.max(predict_prices)*1.2, np.max(real_prices[:, 0])*1.2))
        plt.savefig(f"./gui/images/svg_images/{company}eval.svg", format="svg", transparent=True)
