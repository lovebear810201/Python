import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


plt.rcParams["font.family"] = 'Arial Unicode MS'
a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
df = pd.read_csv(r'/Users/mars/Desktop/python專題報告/[1版]台灣景點旅遊人數統計/台灣景點旅遊人數統計.csv', encoding='big5')

rows = (df['年別'] == 2019) & (df['縣市別'] == '臺北市')
columns = ['細分', '1月', '2月', '3月']
result = df.loc[rows, columns].head(10)
result.set_index('細分', inplace=True)
print(result)

#折線圖


chart = result.plot(title='2019年臺北市各景點旅客人數',  #圖表標題
                    xlabel='細分(景點名稱)',  #x軸說明文字
                    ylabel='人數',  #y軸說明文字
                    legend=True,  # 是否顯示圖例
                    figsize=(10, 10))  # 圖表大小
plt.show()



#折線圖2(待更新)

from matplotlib.font_manager import FontProperties
 
chart = result.plot(figsize=(10, 5))  # 圖表大小
font = FontProperties(fname=r'/System/Library/Fonts/PingFang.ttc')
 
for label in chart.get_xticklabels():
    label.set_fontproperties(font)  # 設定x軸每一個細分(景點名稱)字型
 
plt.title('2019年臺北市各景點旅客人數', fontproperties=font)  #圖表標題
plt.xlabel('細分(景點名稱)', fontproperties=font)  #x軸說明文字
plt.ylabel('人數', fontproperties=font)  #y軸說明文字
plt.legend(prop=font)  #圖例
 
plt.show()

