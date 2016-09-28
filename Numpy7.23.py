#-*- coding:utf-8 -*-
import numpy as np
import scipy as sp
from scipy import stats
from scipy.stats import scoreatpercentile
data = np.loadtxt("test11.csv",delimiter=',',usecols=(1,),skiprows=1,unpack=True) #usecols为读取第2列，skiprows=1为跳过第一行
#print(data)
print(data.max())  		#data的最大值
print(np.max(data)) 		#data的最大值
print(data.min())			#最小值
print(np.min(data))			#最小值
print(data.mean())			#平均值
print(np.mean(data))		#平均值
print(data.std())			#方差	
print(np.std(data))			#方差	 #有偏的
print(np.median(data))		#中位数
print(sp.stats.scoreatpercentile(data,50)) #50%中位数