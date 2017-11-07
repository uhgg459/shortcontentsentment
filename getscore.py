import copy
import pandas as pd
df_testrain=pd.read_csv('getmodel1.csv',encoding="gbk")
df_train = pd.read_excel('泰一指尚训练集.xlsx')  

#要评的文件 df_testrain = pd.read_excel('***.xlsx')  

# a) 情感匹配正确数量：tp
# b) 情感匹配错误数量：fp 
# c) 情感匹配漏判数量：fn1
# d) 情感匹配多判数量：fn2
tp,fp,fn1,fn2=0,0,0,0
for i in range(0,df_train.shape[0]):
	theme=df_train['theme-主题'][i]
	sentiment_anls=df_train['sentiment_anls-情感正负面'][i]
	themece=df_testrain['theme-主题'][i]
	sentiment_anlsce=df_testrain['sentiment_anls-情感正负面'][i]

	#判读主题是否为空，若为空，进行分析。若待测的不为空，
    
	if type(theme)!=type('str'):
		if type(themece)==type('str'):
			themece=themece.strip().split(';')[:-1]
			fn2+=len(themece)

		continue

	theme=theme.strip().split(';')[:-1]
	sentiment_anls=sentiment_anls.strip().split(';')[:-1]
	themece=themece.strip().split(';')[:-1]
	sentiment_anlsce=sentiment_anlsce.strip().split(';')[:-1]

	#构造=字典
	theme_sentiment,theme_sentimentce={},{};
	for indexword in range(len(theme)):
		theme_sentiment[theme[indexword]]=sentiment_anls[indexword]
	for indexwordce in range(len(themece)):
		theme_sentimentce[themece[indexwordce]]=sentiment_anlsce[indexwordce]
		
	for key,values in theme_sentiment.items():
		if key not  in theme_sentimentce:
			fn1+=1
		else:
			if values!=theme_sentimentce[key]:
				fp+=1
			else:tp+=1
			theme_sentimentce.pop(key)  #去除已经匹配
	fn2+=len(theme_sentimentce)  #加成残余的

# 准确率：P=tp/(tp+fp+fn2)
# 召回率：R=tp/( tp+fp+fn1)
# Fβ的数学定义如下：Fβ=(1+)∗P∗R/(∗P+R)
# β=1
P=tp/(tp+fp+fn2)
R=tp/(tp+fp+fn1)
FB=(1+1**2)*P*R/(1**2*P+R)
print("P:"+str(P)+" R:"+str(R)+" FB:"+str(FB))
print( 'ok')






