import os
import numpy as np
import pandas as pd
import datetime as dt

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
        cells = 270
        model = Sequential()
        model.add(LSTM(units = cells, return_sequences=True, activation='tanh', recurrent_activation='sigmoid', input_shape = (7, 45)))
        model.add(Dropout(0.1))
        model.add(LSTM(units = cells, return_sequences=True, activation='tanh', recurrent_activation='sigmoid'))
        model.add(Dropout(0.1))
        model.add(LSTM(units = cells))
        model.add(Dropout(0.1))
        model.add(Dense(units = len(cols_y))) 
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
    
    def Crawlagain(self):
        companies = ["FPT", "CTG", "LCG"]
        end = dt.datetime.now().strftime("%Y-%m-%d") 
        start = (dt.datetime.now() - dt.timedelta(days = 3)).strftime("%Y-%m-%d") 
        for company in companies:
            df = pd.read_csv(f"./data/prepaired/{company}pre.csv", encoding = "utf-8")
            add = vnstock.stock_historical_data(symbol = company, start_date = start, end_date = end)
            if (add['Open'][0] - add['Close'][0]) != df['O-C'][len(df) -1]:
                #Candlesticks
                add['H-L'] = add['High'] - add['Low']
                
                add['O-C'] = df['Open'] - df['Close']
                #Labels
                MA1 = 5
                MA2 = 10
                MA3 = 15
                MA4 = 20
                MA5 = 25
                MA6 = 30
                #Median
                add[f'ME_{MA1}'] = add['Close'].rolling(window = MA1).median()
                add[f'ME_{MA2}'] = add['Close'].rolling(window = MA2).median()
                add[f'ME_{MA3}'] = add['Close'].rolling(window = MA3).median()
                add[f'ME_{MA4}'] = add['Close'].rolling(window = MA4).median()
                add[f'ME_{MA5}'] = add['Close'].rolling(window = MA5).median()
                add[f'ME_{MA6}'] = add['Close'].rolling(window = MA6).median()
                #Rank 
                add[f'RANK_{MA1}'] = add['Close'].rolling(window = MA1).rank()
                add[f'RANK_{MA2}'] = add['Close'].rolling(window = MA2).rank()
                add[f'RANK_{MA3}'] = add['Close'].rolling(window = MA3).rank()
                add[f'RANK_{MA4}'] = add['Close'].rolling(window = MA4).rank()
                add[f'RANK_{MA5}'] = add['Close'].rolling(window = MA5).rank()
                add[f'RANK_{MA6}'] = add['Close'].rolling(window = MA6).rank()
                #Var
                add[f'VAR_{MA1}'] = add['Close'].rolling(window = MA1).var()
                add[f'VAR_{MA2}'] = add['Close'].rolling(window = MA2).var()
                add[f'VAR_{MA3}'] = add['Close'].rolling(window = MA3).var()
                add[f'VAR_{MA4}'] = add['Close'].rolling(window = MA4).var()
                add[f'VAR_{MA5}'] = add['Close'].rolling(window = MA5).var()
                add[f'VAR_{MA6}'] = add['Close'].rolling(window = MA6).var()
                #Simple moving average
                add[f'SMA_{MA1}'] = add['Close'].rolling(window = MA1).mean()
                add[f'SMA_{MA2}'] = add['Close'].rolling(window = MA2).mean()
                add[f'SMA_{MA3}'] = add['Close'].rolling(window = MA3).mean()
                add[f'SMA_{MA4}'] = add['Close'].rolling(window = MA4).mean()
                add[f'SMA_{MA5}'] = add['Close'].rolling(window = MA5).mean()
                add[f'SMA_{MA6}'] = add['Close'].rolling(window = MA6).mean()
                #Standard deviation
                add[f'SD_{MA1}'] = add['Close'].rolling(window = MA1).std()
                add[f'SD_{MA2}'] = add['Close'].rolling(window = MA2).std()
                add[f'SD_{MA3}'] = add['Close'].rolling(window = MA3).std()
                add[f'SD_{MA4}'] = add['Close'].rolling(window = MA4).std()
                add[f'SD_{MA5}'] = add['Close'].rolling(window = MA5).std()
                add[f'SD_{MA6}'] = add['Close'].rolling(window = MA6).std()
                #Skewness
                add[f'Ske_{MA1}'] = add['Close'].rolling(window = MA1).skew()
                add[f'Ske_{MA2}'] = add['Close'].rolling(window = MA2).skew()
                add[f'Ske_{MA3}'] = add['Close'].rolling(window = MA3).skew()
                add[f'Ske_{MA4}'] = add['Close'].rolling(window = MA4).skew()
                add[f'Ske_{MA5}'] = add['Close'].rolling(window = MA5).skew()
                add[f'Ske_{MA6}'] = add['Close'].rolling(window = MA6).skew()
                #Kurtosis
                add[f'Kur_{MA1}'] = add['Close'].rolling(window = MA1).kurt()
                add[f'Kur_{MA2}'] = add['Close'].rolling(window = MA2).kurt()
                add[f'Kur_{MA3}'] = add['Close'].rolling(window = MA3).kurt()
                add[f'Kur_{MA4}'] = add['Close'].rolling(window = MA4).kurt()
                add[f'Kur_{MA5}'] = add['Close'].rolling(window = MA5).kurt()
                add[f'Kur_{MA6}'] = add['Close'].rolling(window = MA6).kurt()
                #Drop missing data
                add.dropna(inplace = True)
                df = pd.concat([df,add])
                Functions.SetLineGraph(self, df,company)

    
    def CrawlCompanies():
        companies = ["FPT", "CTG", "LCG"]
        end = dt.datetime.now().strftime("%Y-%m-%d") 
        start = (dt.datetime.now() - dt.timedelta(days=180)).strftime("%Y-%m-%d") 
        for company in companies:
            df = vnstock.stock_historical_data(symbol = company, start_date = start, end_date = end)
            #Candlesticks
            df['H-L'] = df['High'] - df['Low']
        
            df['O-C'] = df['Open'] - df['Close']
            #Labels
            MA1 = 5
            MA2 = 10
            MA3 = 15
            MA4 = 20
            MA5 = 25
            MA6 = 30
            #Median
            df[f'ME_{MA1}'] = df['Close'].rolling(window = MA1).median()
            df[f'ME_{MA2}'] = df['Close'].rolling(window = MA2).median()
            df[f'ME_{MA3}'] = df['Close'].rolling(window = MA3).median()
            df[f'ME_{MA4}'] = df['Close'].rolling(window = MA4).median()
            df[f'ME_{MA5}'] = df['Close'].rolling(window = MA5).median()
            df[f'ME_{MA6}'] = df['Close'].rolling(window = MA6).median()
            #Rank 
            df[f'RANK_{MA1}'] = df['Close'].rolling(window = MA1).rank()
            df[f'RANK_{MA2}'] = df['Close'].rolling(window = MA2).rank()
            df[f'RANK_{MA3}'] = df['Close'].rolling(window = MA3).rank()
            df[f'RANK_{MA4}'] = df['Close'].rolling(window = MA4).rank()
            df[f'RANK_{MA5}'] = df['Close'].rolling(window = MA5).rank()
            df[f'RANK_{MA6}'] = df['Close'].rolling(window = MA6).rank()
            #Var
            df[f'VAR_{MA1}'] = df['Close'].rolling(window = MA1).var()
            df[f'VAR_{MA2}'] = df['Close'].rolling(window = MA2).var()
            df[f'VAR_{MA3}'] = df['Close'].rolling(window = MA3).var()
            df[f'VAR_{MA4}'] = df['Close'].rolling(window = MA4).var()
            df[f'VAR_{MA5}'] = df['Close'].rolling(window = MA5).var()
            df[f'VAR_{MA6}'] = df['Close'].rolling(window = MA6).var()
            #Simple moving average
            df[f'SMA_{MA1}'] = df['Close'].rolling(window = MA1).mean()
            df[f'SMA_{MA2}'] = df['Close'].rolling(window = MA2).mean()
            df[f'SMA_{MA3}'] = df['Close'].rolling(window = MA3).mean()
            df[f'SMA_{MA4}'] = df['Close'].rolling(window = MA4).mean()
            df[f'SMA_{MA5}'] = df['Close'].rolling(window = MA5).mean()
            df[f'SMA_{MA6}'] = df['Close'].rolling(window = MA6).mean()
            #Standard deviation
            df[f'SD_{MA1}'] = df['Close'].rolling(window = MA1).std()
            df[f'SD_{MA2}'] = df['Close'].rolling(window = MA2).std()
            df[f'SD_{MA3}'] = df['Close'].rolling(window = MA3).std()
            df[f'SD_{MA4}'] = df['Close'].rolling(window = MA4).std()
            df[f'SD_{MA5}'] = df['Close'].rolling(window = MA5).std()
            df[f'SD_{MA6}'] = df['Close'].rolling(window = MA6).std()
            #Skewness
            df[f'Ske_{MA1}'] = df['Close'].rolling(window = MA1).skew()
            df[f'Ske_{MA2}'] = df['Close'].rolling(window = MA2).skew()
            df[f'Ske_{MA3}'] = df['Close'].rolling(window = MA3).skew()
            df[f'Ske_{MA4}'] = df['Close'].rolling(window = MA4).skew()
            df[f'Ske_{MA5}'] = df['Close'].rolling(window = MA5).skew()
            df[f'Ske_{MA6}'] = df['Close'].rolling(window = MA6).skew()
            #Kurtosis
            df[f'Kur_{MA1}'] = df['Close'].rolling(window = MA1).kurt()
            df[f'Kur_{MA2}'] = df['Close'].rolling(window = MA2).kurt()
            df[f'Kur_{MA3}'] = df['Close'].rolling(window = MA3).kurt()
            df[f'Kur_{MA4}'] = df['Close'].rolling(window = MA4).kurt()
            df[f'Kur_{MA5}'] = df['Close'].rolling(window = MA5).kurt()
            df[f'Kur_{MA6}'] = df['Close'].rolling(window = MA6).kurt()
            #Drop missing data
            df.dropna(inplace = True)
            df.to_csv(f"./data/prepaired/{company}pre.csv", encoding = "utf-8")
        
    def SetLineGraph(self, df, company):
        MA1 = 5
        MA2 = 10
        MA3 = 15
        MA4 = 20
        MA5 = 25
        MA6 = 30
        scaler_x = MinMaxScaler(feature_range = (0, 1))
        scaler_y = MinMaxScaler(feature_range = (0, 1))
        cols_x = ['H-L', 'O-C', 'Volume', f'ME_{MA1}', f'ME_{MA2}', f'ME_{MA3}', f'ME_{MA4}', f'ME_{MA5}', f'ME_{MA6}', f'VAR_{MA1}', f'VAR_{MA2}', f'VAR_{MA3}', f'VAR_{MA4}', f'VAR_{MA5}', f'VAR_{MA6}', f'RANK_{MA1}', f'RANK_{MA2}', f'RANK_{MA3}', f'RANK_{MA4}', f'RANK_{MA5}', f'RANK_{MA6}', f'SMA_{MA1}', f'SMA_{MA2}', f'SMA_{MA3}', f'SMA_{MA4}', f'SMA_{MA5}', f'SMA_{MA6}', f'SD_{MA1}' ,f'SD_{MA2}', f'SD_{MA3}', f'SD_{MA4}', f'SD_{MA5}', f'SD_{MA6}', f'Ske_{MA1}', f'Ske_{MA2}', f'Ske_{MA3}', f'Ske_{MA4}', f'Ske_{MA5}', f'Ske_{MA6}', f'Kur_{MA1}', f'Kur_{MA2}', f'Kur_{MA3}', f'Kur_{MA4}', f'Kur_{MA5}', f'Kur_{MA6}']
        cols_y = ['Close']
        scaled_data_x = scaler_x.fit_transform(df[cols_x].values.reshape(-1, len(cols_x))) 
        scaled_data_y = scaler_y.fit_transform(df[cols_y].values.reshape(-1, len(cols_y)))
        self.model = load_model(f"./gui/models/{company}.h5")
        
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
        fig, ax = plt.subplots(figsize=(12, 6))
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
    
    def Evaluation(self, df, company):
        MA1 = 5
        MA2 = 10
        MA3 = 15
        MA4 = 20
        MA5 = 25
        MA6 = 30
        scaler_x = MinMaxScaler(feature_range = (0, 1))
        scaler_y = MinMaxScaler(feature_range = (0, 1))
        cols_x = ['H-L', 'O-C', 'Volume', f'ME_{MA1}', f'ME_{MA2}', f'ME_{MA3}', f'ME_{MA4}', f'ME_{MA5}', f'ME_{MA6}', f'VAR_{MA1}', f'VAR_{MA2}', f'VAR_{MA3}', f'VAR_{MA4}', f'VAR_{MA5}', f'VAR_{MA6}', f'RANK_{MA1}', f'RANK_{MA2}', f'RANK_{MA3}', f'RANK_{MA4}', f'RANK_{MA5}', f'RANK_{MA6}', f'SMA_{MA1}', f'SMA_{MA2}', f'SMA_{MA3}', f'SMA_{MA4}', f'SMA_{MA5}', f'SMA_{MA6}', f'SD_{MA1}' ,f'SD_{MA2}', f'SD_{MA3}', f'SD_{MA4}', f'SD_{MA5}', f'SD_{MA6}', f'Ske_{MA1}', f'Ske_{MA2}', f'Ske_{MA3}', f'Ske_{MA4}', f'Ske_{MA5}', f'Ske_{MA6}', f'Kur_{MA1}', f'Kur_{MA2}', f'Kur_{MA3}', f'Kur_{MA4}', f'Kur_{MA5}', f'Kur_{MA6}']
        cols_y = ['Close']
        scaled_data_x = scaler_x.fit_transform(df[cols_x].values.reshape(-1, len(cols_x))) 
        scaled_data_y = scaler_y.fit_transform(df[cols_y].values.reshape(-1, len(cols_y)))
        pre_day = 7
        x_total = [] 
        y_total = []
        for i in range(pre_day, len(df)):
            x_total.append(scaled_data_x[i - pre_day : i])
            y_total.append(scaled_data_y[i])
        test_size = 60
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
        fig, ax = plt.subplots(figsize=(12, 6))
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
