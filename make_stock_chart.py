import pandas as pd
import mplfinance as mpf

data = pd.read_csv('6201_2019.csv',header = 1,engine="python")

#カラム名を英語に変更
data.columns = ["date","Open","High","Low","Close","Volume",""]
#必要なカラムのみ取り出し
data = data[["date","Open","High","Low","Close","Volume"]]
#dateをdatetime型に変更
data["date"] = pd.to_datetime(data["date"])
#dateをindex名に
data = data.set_index('date')

mpf.plot(data,volume = True,type = 'candle',mav = (5,20,50))
