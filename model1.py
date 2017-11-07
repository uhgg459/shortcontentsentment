import bocff_1
import pandas as pd

def generatewordcouple(shortcontent,wordtupledict):
	#生成词对  目前是穷举法
	wordcouplearray,wordcouplearraydict=[],{}	
	for i in range(len(shortcontent)):fgdsfdsf
		for j in range(i+1,len(shortcontent)):sdfldf
			wordcouplearray.append((shortcontent[i],shortcontent[j]))
	#归纳所有词对的次数
	for wordcouple in wordcouplearray:
		if wordcouple in  wordtupledict:
			wordcouplearraydict[wordcouple]=wordtupledict[wordcouple]
	return wordcouplearraydict
	
def generatesimgplewordcouple(shortcontent,wordtupledict):
	wordcouplearraydict={}
	wordcouplearray=[("NULL",simpleword) for simpleword in shortcontent]
	for wordcouple in wordcouplearray:
		if wordcouple in  wordtupledict:
			wordcouplearraydict[wordcouple]=wordtupledict[wordcouple]
	return wordcouplearraydict

if __name__ == '__main__':
	
	#df_train = pd.read_excel('泰一指尚训练集.xlsx','r')
	finalfile=open("getmodel1.csv",'w')
	finalfile.write("sentiment_word-情感关键词,sentiment_anls-情感正负面\n")
	finalfile.flush()
	wordtupledict=bocff_1.getdump('cidui.pkl')
	df_word=open("AfterCut_train.txt",'r',encoding='utf8')
	while True:
		lines=df_word.readline()
		if not lines:
			break
		contentarray=lines.split(';')
		findaltheme_sentimentarray=[]
		
		wordcouplearray=[]
		#遍历每个短评
		for shortcontent in contentarray:
			shortcontent=shortcontent.split(' ')
			count=0
			
			
			wordcouplearraydict=generatewordcouple(shortcontent,wordtupledict)
			#如果短评还有词对的化
			while len(wordcouplearraydict)>0 and count<2:
				maxvalue=max(wordcouplearraydict.values())
				newindex=""
				for getindex in wordcouplearraydict.keys():
					if maxvalue==wordcouplearraydict[getindex]:
						newindex=getindex
						break
				if newindex!=0:
					newtheme_sentiment=list(newindex)
					findaltheme_sentimentarray.append(newtheme_sentiment)
					count=count+1
					shortcontent.remove(newindex[0])
					shortcontent.remove(newindex[1])
					wordcouplearraydict=generatewordcouple(shortcontent,wordtupledict)
		   
			wordcouplearraydict=generatesimgplewordcouple(shortcontent,wordtupledict)
			while len(wordcouplearraydict)>0 and count<2:
				maxvalue=max(wordcouplearraydict.values())
				newindex=""
				for getindex in wordcouplearraydict.keys():
					if maxvalue==wordcouplearraydict[getindex]:
						newindex=getindex
						break
				if newindex!=0:
					newtheme_sentiment=newindex
					findaltheme_sentimentarray.append(newtheme_sentiment)
					count=count+1
					shortcontent.remove(newindex[1])
					wordcouplearraydict=generatesimgplewordcouple(shortcontent,wordtupledict)
			
		if len(findaltheme_sentimentarray)==0:
			finalfile.write('\n')
			finalfile.flush()
			continue
		for newtheme_sentiment in  findaltheme_sentimentarray:
			finalfile.write(newtheme_sentiment[0]+';')
			finalfile.flush()
		finalfile.write(',')
		for newtheme_sentiment in  findaltheme_sentimentarray:
			finalfile.write(newtheme_sentiment[1]+';')
			finalfile.flush()
		finalfile.write('\n')

		

	finalfile.close()

	print( 'ok')



