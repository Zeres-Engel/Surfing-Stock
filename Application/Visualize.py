import sys
import numpy as np
import pandas as pd

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM



class MyWidget(QWidget):
    def __init__(self, company):
        super().__init__()
        self.company = company
        self.df = pd.read_csv(f".\gui\data\prepaired\{company}pre.csv", encoding = "utf-8")
        MA1 = 7
        MA2 = 14
        MA3 = 21
        MA4 = 28
        self.scaler_x = MinMaxScaler(feature_range = (0, 1))
        self.scaler_y = MinMaxScaler(feature_range = (0, 1))
        self.cols_x = ['Close','H-L', 'O-C', 'Volume', f'ME_{MA1}', f'ME_{MA2}', f'ME_{MA3}', f'ME_{MA4}', f'VAR_{MA1}', f'VAR_{MA2}', f'VAR_{MA3}', f'VAR_{MA4}', f'RANK_{MA1}', f'RANK_{MA2}', f'RANK_{MA3}', f'RANK_{MA4}', f'SMA_{MA1}', f'SMA_{MA2}', f'SMA_{MA3}', f'SMA_{MA4}', f'SD_{MA1}' ,f'SD_{MA2}', f'SD_{MA3}', f'SD_{MA4}', f'Ske_{MA1}', f'Ske_{MA2}', f'Ske_{MA3}', f'Ske_{MA4}', f'Kur_{MA1}', f'Kur_{MA2}', f'Kur_{MA3}', f'Kur_{MA4}',] #Variables for training
        self.cols_y = ['Close','H-L', 'O-C', 'Volume', f'ME_{MA1}', f'ME_{MA2}', f'ME_{MA3}', f'ME_{MA4}', f'VAR_{MA1}', f'VAR_{MA2}', f'VAR_{MA3}', f'VAR_{MA4}', f'RANK_{MA1}', f'RANK_{MA2}', f'RANK_{MA3}', f'RANK_{MA4}', f'SMA_{MA1}', f'SMA_{MA2}', f'SMA_{MA3}', f'SMA_{MA4}', f'SD_{MA1}' ,f'SD_{MA2}', f'SD_{MA3}', f'SD_{MA4}', f'Ske_{MA1}', f'Ske_{MA2}', f'Ske_{MA3}', f'Ske_{MA4}', f'Kur_{MA1}', f'Kur_{MA2}', f'Kur_{MA3}', f'Kur_{MA4}',]
        scaled_data_x = self.scaler_x.fit_transform(self.df[self.cols_x].values.reshape(-1, len(self.cols_x))) 
        scaled_data_y = self.scaler_y.fit_transform(self.df[self.cols_y].values.reshape(-1, len(self.cols_y)))
        model = Sequential()
        cells = 180
        model.add(LSTM(units = cells, return_sequences = True, activation='tanh', recurrent_activation='sigmoid', input_shape = (90, 32))) #input traning date and predicting date 
        model.add(Dropout(0.1))
        model.add(LSTM(units = cells))
        model.add(Dropout(0.1))
        model.add(Dense(units = 32))
        self.model = load_model(f".\gui\model\{company}.h5")
        self.real_prices = self.df[len(self.df)-31:]['Close'].values.reshape(-1, 1)
        self.real_prices = np.array(self.real_prices)
        self.real_prices = self.real_prices.reshape(self.real_prices.shape[0], 1)
        self.predict_prices = self.real_prices
        x_predict = self.df[len(self.df)-90:][self.cols_x].values.reshape(-1, len(self.cols_x))
        x_predict = self.scaler_x.transform(x_predict)
        x_predict = np.array(x_predict)
        x_predict = x_predict.reshape(1, x_predict.shape[0], len(self.cols_x))
        for i in range(30):
            prediction = self.model.predict(x_predict)
            prediction = self.scaler_y.inverse_transform(prediction)
            self.predict_prices = np.append(self.predict_prices, [prediction[0][0]])
            for i in range(30):
                x_predict[0][i] = x_predict[0][i + 1]
            prediction = self.scaler_x.transform(prediction)
            x_predict[0][30] = prediction

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        self.setLayout(layout)

        self.ax = self.figure.add_subplot(111)
        self.ax.plot(self.predict_prices, label='z')
        self.ax.plot(self.real_prices, label='y')
        self.ax.legend()

app = QApplication(sys.argv)
window = QMainWindow()
widget = MyWidget('FPT')
window.setCentralWidget(widget)
window.show()
sys.exit(app.exec())
