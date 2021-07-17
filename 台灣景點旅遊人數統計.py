import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#from matplotlib.font_manager import FontProperties
#font = FontProperties(fname=r'NotoSansCJKtc-Medium.otf')
plt.rcParams["font.family"] = 'Arial Unicode MS'
a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
#plt.rcParams['font.sans-serif'] = ['Arial Black'] # 用来正常显示中文标签
#plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号
df = pd.read_csv(r'/Users/mars/Desktop/python專題報告/歷年國內主要觀光遊憩據點遊客人數月別統計.csv', encoding='big5')

rows = (df['年別'] == 2019) & (df['縣市別'] == '臺北市')
columns = ['細分', '1月', '2月', '3月']
result = df.loc[rows, columns].head(10)
result.set_index('細分', inplace=True)
print(result)
#Pandas套件的plot()繪圖方法(Method)預設為折線圖
chart = result.plot(title='2019年臺北市各景點旅客人數',  #圖表標題
                    xlabel='細分(景點名稱)',  #x軸說明文字
                    ylabel='人數',  #y軸說明文字
                    legend=True,  # 是否顯示圖例
                    figsize=(10, 5))  # 圖表大小
plt.show()

#長條圖
 
chart = result.plot(kind='bar',  #圖表類型
		    title='2019年臺北市各景點旅客人數',  #圖表標題
                    xlabel='細分(景點名稱)',  #x軸說明文字
                    ylabel='人數',  #y軸說明文字
                    legend=True,  # 是否顯示圖例
                    figsize=(10, 5))  # 圖表大小
plt.show()


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

