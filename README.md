# SURFING STOCK

<div>
  <p align="center">
    <img src="images/logo.svg" width="800"> 
  </p>
</div>

Welcome to Surfing Stock, an application built using the [QT](https://en.wikipedia.org/wiki/Qt_(software)) library that utilizes a prediction model for stock prices based on an [LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory) neural network. This app provides users with the ability to predict the stock prices for the following day using data from the seven previous days.

With its user-friendly interface, Surfing Stock is easy to use and provides users with reliable and insightful predictions. By utilizing the power of deep learning, Surfing Stock can help users make informed decisions in their investment strategies.

<p align="center">
  <img src="https://img.shields.io/badge/OS-Windows-red?style=flat&logo=" />
  <img src="https://img.shields.io/badge/Python-v3.10.9-blue?style=flat&logo=python" />
  <img src="https://img.shields.io/badge/Neural%20Network-LSTM-yellow?style=flat&logo=tensorflow" />
  <img src="https://img.shields.io/badge/QT-6.3.2-green?style=flat&logo=qt" />
  <a href="https://github.com/Zeres-Engel"><img src="https://img.shields.io/github/followers/Zeres-Engel.svg?style=social&label=Follow" /></a>
</p>

# Table of Content
- [Overview](#overview)
- [Building the Model](#building-the-model)
    - [Data Understanding](#data-understanding)
    - [Data Preprocessing](#data-preprocessing)
    - [Layers (LSTM)](#layers-lstm)
    - [Optimizer (Adam)](#optimizer-adam)
- [Deploying the Product](#deploying-the-product)
    - [User Interface](#user-interface)
    - [Configuration](#configuration)

## Overview

The app is designed to automatically scrape stock data using the VNStock API and predict the stock price for the following day. The app displays the predicted stock price using a chart.
<img src="images/overview.png" width="800">

## Building the Model

In addition to extracting the 31 feature columns, the data is also split into training and testing sets. The training set contains data from the first 80% of the time series, while the testing set contains the remaining 20%. This allows the model to learn patterns and trends from past stock prices and test its ability to make accurate predictions on future stock prices.

After building and training the LSTM model, it is saved to disk as a .h5 file. This allows for easy and quick access to the model for future use in the Surfing Stock app.

```python
from keras.models import save_model

save_model(model, f"model/{company}.h5", include_optimizer = True)
```

### Data Understanding

The data is collected using the VNStock API, and the following data variables are used for predicting the stock price:

- Date
- Open
- High
- Low
- Close
- Volume

### Data Preprocessing

Data preprocessing is performed to extract 31 feature columns from the raw data. These features are then used to build the LSTM model.

- Volume
- Candlestick patterns
- Median prices
- Simple moving averages
- Skewness
- Kurtosis
-Technical indicators (RSI, MACD, etc.)
By extracting and using these features, we can better capture the patterns and trends in the stock price data and improve the accuracy of our predictions.

### Layers (LSTM)

The LSTM model is used to predict the stock price using the 31 extracted feature columns.

```python
model = Sequential()
cells = 248
model.add(LSTM(units = cells, activation='tanh', recurrent_activation='sigmoid', input_shape = (x_train.shape[1], x_train.shape[2])))
model.add(Dropout(0.1))
model.add(Dense(units = len(cols_y))) 
```

### Optimizer (Adam)

Using the Adam optimizer for stock price prediction models has several benefits, including stability, adaptiveness, and efficiency. It helps the model converge faster, achieve better results, and optimize more efficiently than other optimizers such as SGD or Adagrad.

```python
model.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['accuracy']) 
history = model.fit(x_train, y_train, epochs = 10, batch_size = 2, use_multiprocessing = True, validation_split=0.2, shuffle=True)
```

## Deploying the Product

To use the Surfing Stock app, users simply need to download and install the required libraries and run the main.py file. The app will automatically scrape stock data and use the saved LSTM model to make predictions for the following day's stock price.

The predicted stock price is displayed on the app's user interface, along with a chart that shows the historical stock prices and the predicted stock price for the next day.

The app also includes a settings menu where users can adjust the time range of the historical stock data displayed on the chart, as well as the time range of the predicted stock price.

Overall, the Surfing Stock app provides a user-friendly and efficient way for users to make informed decisions in their investment strategies by utilizing the power of deep learning to predict stock prices.

### User Interface

The product has a user interface that displays the predicted stock price using a chart. The chart is designed to be easy to read and understand.

Closing price chart:

<img src="images/overview.png" width="800">

Model quality rating chart:

<img src="images/evaluate.png" width="800">

### Configuration

The Surfing Stock app has a user-friendly interface that displays predicted stock prices using a chart. To use the app, users need to install the required libraries, which are listed in the requirements.txt file.
