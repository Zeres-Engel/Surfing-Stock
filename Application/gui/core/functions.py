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
    def set_svg_icon(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/svg_icons/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon
    def set_svg_image(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/svg_images/"
        path = os.path.join(app_path, folder)
        image = os.path.normpath(os.path.join(path, icon_name))
        return image
    def set_image(image_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/images/"
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
    def SetLineGraph(company):
        df = pd.read_csv(f"./gui/data/prepaired/{company}pre.csv", encoding = "utf-8")
        MA1 = 7
        MA2 = 14
        MA3 = 21
        MA4 = 28
        scaler_x = MinMaxScaler(feature_range = (0, 1))
        scaler_y = MinMaxScaler(feature_range = (0, 1))
        cols_x = ['Close','H-L', 'O-C', 'Volume', f'ME_{MA1}', f'ME_{MA2}', f'ME_{MA3}', f'ME_{MA4}', f'VAR_{MA1}', f'VAR_{MA2}', f'VAR_{MA3}', f'VAR_{MA4}', f'RANK_{MA1}', f'RANK_{MA2}', f'RANK_{MA3}', f'RANK_{MA4}', f'SMA_{MA1}', f'SMA_{MA2}', f'SMA_{MA3}', f'SMA_{MA4}', f'SD_{MA1}' ,f'SD_{MA2}', f'SD_{MA3}', f'SD_{MA4}', f'Ske_{MA1}', f'Ske_{MA2}', f'Ske_{MA3}', f'Ske_{MA4}', f'Kur_{MA1}', f'Kur_{MA2}', f'Kur_{MA3}', f'Kur_{MA4}',] #Variables for training
        cols_y = ['Close','H-L', 'O-C', 'Volume', f'ME_{MA1}', f'ME_{MA2}', f'ME_{MA3}', f'ME_{MA4}', f'VAR_{MA1}', f'VAR_{MA2}', f'VAR_{MA3}', f'VAR_{MA4}', f'RANK_{MA1}', f'RANK_{MA2}', f'RANK_{MA3}', f'RANK_{MA4}', f'SMA_{MA1}', f'SMA_{MA2}', f'SMA_{MA3}', f'SMA_{MA4}', f'SD_{MA1}' ,f'SD_{MA2}', f'SD_{MA3}', f'SD_{MA4}', f'Ske_{MA1}', f'Ske_{MA2}', f'Ske_{MA3}', f'Ske_{MA4}', f'Kur_{MA1}', f'Kur_{MA2}', f'Kur_{MA3}', f'Kur_{MA4}',]
        scaled_data_x = scaler_x.fit_transform(df[cols_x].values.reshape(-1, len(cols_x))) 
        scaled_data_y = scaler_y.fit_transform(df[cols_y].values.reshape(-1, len(cols_y)))
        model = Sequential()
        cells = 180
        model.add(LSTM(units = cells, return_sequences = True, activation='tanh', recurrent_activation='sigmoid', input_shape = (90, 32))) #input traning date and predicting date 
        model.add(Dropout(0.1))
        model.add(LSTM(units = cells))
        model.add(Dropout(0.1))
        model.add(Dense(units = 32))
        model = load_model(f".\gui\model\{company}.h5")
        real_prices = df[len(df)-31:]['Close'].values.reshape(-1, 1)
        real_prices = np.array(real_prices)
        real_prices = real_prices.reshape(real_prices.shape[0], 1)
        predict_prices = real_prices
        x_predict = df[len(df)-90:][cols_x].values.reshape(-1, len(cols_x))
        x_predict = scaler_x.transform(x_predict)
        x_predict = np.array(x_predict)
        x_predict = x_predict.reshape(1, x_predict.shape[0], len(cols_x))
        for i in range(30):
            prediction = model.predict(x_predict)
            prediction = scaler_y.inverse_transform(prediction)
            predict_prices = np.append(predict_prices, [prediction[0][0]])
            for i in range(30):
                x_predict[0][i] = x_predict[0][i + 1]
            prediction = scaler_x.transform(prediction)
            x_predict[0][30] = prediction
        plt.figure(figsize=(10, 5))
        plt.plot(predict_prices, color="blue", label=f"Predicted {company}'s prices")
        plt.plot(real_prices, color="red", label=f"Real {company}'s prices")
        plt.title(f"{company}'s prices for 10 years")
        plt.xlabel("Days")
        plt.ylabel("Stock Prices")
        plt.legend()
        plt.savefig(f".\gui\images\svg_images\{company}.svg", format="svg")