import pandas as pd
import copy
import pickle
import pprint
# import numpy as np
# import jieba
# import jieba.posseg as pseg
# import jieba.analyse
# import re
def gettheme_sentiment(df_train):
	#df_train = pd.read_excel('泰一指尚训练集.xlsx')
	#df_example = copy.deepcopy(df_train)
	wordtuple={}
	for i in range(0,df_train.shape[0]):
		zhu=df_train['theme-主题'][i]
		qinggan=df_train['sentiment_word-情感关键词'][i]
		if type(zhu)!=type('str'):
			continue
		
		zhu=zhu.strip().split(';')[:-1]
		qinggan=qinggan.strip().split(';')[:-1]
		
		for j in range(0,len(zhu)):
			if (zhu[j],qinggan[j]) not in wordtuple:
				wordtuple[(zhu[j],qinggan[j])]=1
			else:wordtuple[(zhu[j],qinggan[j])]+=1
	return wordtuple

def pickdump(wordtuple,filename):  #将数据保存到文件
	f = open(filename, 'wb')
	pickle.dump(wordtuple, f)
	f.close()

def getdump(fw):
	pkl_file = open(fw, 'rb')
	data1 = pickle.load(pkl_file)
	pkl_file.close()
	return data1

# if __name__ == '__main__':
# 	fw='cidui.pkl'
# 	df_train= pd.read_excel('泰一指尚训练集.xlsx')
# 	wordtuple=gettheme_sentiment(df_train)
# 	pickdump(wordtuple, fw)
# 	getdump(fw)
# 	print( 'ok')


