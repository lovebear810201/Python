import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#匯入資料ＣＳＶ

a = pd.read_csv(r"/Users/mars/Desktop/python專題報告/槍砲彈藥刀械資料分析.csv",encoding='utf8')
a.head(3)    # 顯示前3筆資料
print(a)



#長條圖



#直方圖
#圓餅圖2
#圓餅圖
#多圖表應用


#匯入csv









#設定中文字型
plt.rcParams['font.family']='DFKai-SB'
plt.rcParams['font.size']=12








#取總數
Tourist_total=Tourist.iloc[43]
#取近10年資料
Tourist_total1=Tourist_total[11:]
#Reset index並增加欄位名稱方便後續處理
Tourist_total2 = pd.DataFrame(Tourist_total1).reset_index()
Tourist_total2.columns = ['year', 'numbers']
#設定X軸Y軸
Tourist_x=Tourist_total2['year']
Tourist_y=Tourist_total2['numbers']
#轉成int
Tourist_y=pd.to_numeric(Tourist_y, errors='coerce')
#設定畫布大小
plt.figure(figsize=(15,10), facecolor='pink')
#設定圖表類型及相關設定
plt.plot(Tourist_x,Tourist_y, 'o-', color = 'pink', label='人數')
plt.legend()
plt.xlabel('年份', fontsize=15)
plt.ylabel('人數(百萬)', fontsize=15)
plt.title('近10年來台旅客人數', fontsize=20)
#顯示圖表
plt.show()