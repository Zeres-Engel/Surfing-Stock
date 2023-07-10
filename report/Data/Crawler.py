import pandas as pd
import datetime as dt
import numpy as np

#API
import vnstock
from vnstock import *



def crawl(company):
    start = "2000-02-15" #Happy new year
    end = today = dt.datetime.now().strftime("%Y-%m-%d") 
    df = vnstock.stock_historical_data(symbol = company, start_date = start, end_date = end)
    df.to_csv(f"./data/raw/{company}.csv",encoding = "utf-8")

if __name__ == "__main__":
    fhandle = open("./data/companylist.txt","r")
    for line in fhandle.readlines():
        company = line.strip()
        print(f"{company}'s stock", end=' ')
        crawl(company)