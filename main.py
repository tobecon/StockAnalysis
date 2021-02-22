import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

fund_data = pd.read_excel("data.xlsx",sheet_name="数据")

subset = fund_data[["日期","上证指数","贵州茅台(600519)"]]
subset.info()
subset = subset.set_index("日期")
dataSeries = subset["2019-03-01":"2019-05-01"]

dataSeries["上证涨跌"] = dataSeries["上证指数"].diff()
dataSeries["上证涨跌百分比"] = (dataSeries["上证涨跌"]/dataSeries["上证指数"].shift(1))*100

dataSeries["股票涨跌"] = dataSeries["贵州茅台(600519)"].diff()
dataSeries["股票涨跌百分比"] = (dataSeries["股票涨跌"]/dataSeries["贵州茅台(600519)"].shift(1))*100

dataSeries["股票-上证"] = dataSeries["股票涨跌百分比"]-dataSeries["上证涨跌百分比"]

acculateDownUp = dict()
dataSeries.info()
previous = 1
for row in dataSeries.itertuples():
    if np.isnan(row[7]):
        continue
    previous = (row[7]/100 +1) * previous
    acculateDownUp[row[0]] = previous

dataSeries["累计涨跌幅百分比"] = pd.Series(acculateDownUp)
print(dataSeries.head(100))
p = dataSeries["累计涨跌幅百分比"].plot(y="累计涨跌幅百分比",x="时间")
p.set_ylabel('累计涨跌幅百分比')
pic = p.get_figure()
pic.savefig("data.png")
# print(shangZ.diff().apply(lambda:))