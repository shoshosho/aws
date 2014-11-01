import pandas as pd
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
import pylab as pl

analy = "data3.csv"
    #ファイルの読み込み
dump = pd.read_csv(analy)
dump2 = pd.read_csv(analy, header=None , names=('a', 'b', 'c', 'd', 'e', 'f'))

line = dump2.ix[:0,:]
lines = line.values
lin = line.T

dump.fillna(0)

plist = []

#項目数の分だけループ回数を指定
for n in range(len(lin)):
    #dumpに格納された変数をリストに格納
    for l in dump:
        plist.append(l)
    #d変数ごとに集計、ヒストグラムを表示する
    plt.hist(dump[plist[n]])
    plt.legend(plist)
    plt.show()
    #hold(False);
    
