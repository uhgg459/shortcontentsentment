import pandas as pd
import numpy as np
import jieba
import jieba.posseg as pseg
import jieba.analyse
import re
from jieba import analyse

df_train = pd.read_excel('泰一指尚训练集.xlsx')
#df_test=pd.read_csv('泰一指尚-评测集.csv',encoding='gbk')

fp = open("AfterCut.txt",'w',encoding='utf8',errors='ignore')#保存关键词
ft=open("traintheme.txt",'w',encoding='utf8',errors='ignore')#保存主题词



tfidf = analyse.extract_tags# 引入TF-IDF关键词抽取接口

def savefile(f,content):
    f.write(content)
    f.write("\n")

# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

# 对句子去除停用词
def movestopwords(sentence):
    stopwords = stopwordslist('ModifiedStopWord.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence:
        if word not in stopwords:#判断词是否在停用词表中
            if((word!= '\t')and(word !='\n')):#保持格式
                if(((word >= u'\u4e00')and(word <= u'\u9fa5'))or(word ==" ")or(word =="；")):#判断是否是汉字
                # if(((word >= u'\u4e00')and(word <= u'\u9fa5'))or(word ==" ")or(word =="；")or(word =="！")or(word =="!")or(word =="？")or(word =="?")):#判断是否是汉字和情感符号
                    outstr += word+" "
    return outstr

def romoveRepetedGap(str,char):#去除指定连续重复符号
    resultStr = str
    tempStr = ''
    strList = list(resultStr)
    for i in range(len(strList)):
        if strList[i] != char:
            tempStr += strList[i]
        elif strList[i] == char and i+1 ==len(strList):
            tempStr += strList[i]
        elif strList[i] == char and strList[i+1] !=char:
            tempStr += strList[i]
        else: continue
    return tempStr

# 根据提取词典添加自定义词
def add_DIY_word(filepath):
    fw=open(filepath, 'r', encoding='utf-8')#读取从训练语料提取的主题词
    for word in fw.readlines():
        word=word.replace("\n","")
        jieba.add_word(word)



add_DIY_word('theme_word.txt')#从提取的主题词添加自定义词
add_DIY_word('sentiment_word.txt')#从提取的情感词添加自定义词

#对评论内容进行分词并保存
for i in range(0,19999):
    print(df_test['content-评论内容'][i])
    tmp_str=str(df_test['content-评论内容'][i]).encode('utf-8').decode('utf-8')
    #去除连续重复符号
    tmp_str=romoveRepetedGap(tmp_str,'!')
    tmp_str=romoveRepetedGap(tmp_str,'！')
    tmp_str=romoveRepetedGap(tmp_str,'?')
    tmp_str=romoveRepetedGap(tmp_str,'？')

    #按指定标点符号分隔字符串并且保留情感标点符号
    # tmp_str=tmp_str.replace('!','!%').replace('！','！%').replace('?','?%').replace('？','？%')
    tmpre=re.split("\.|，|。|,|!|！|？|\?", tmp_str)

    #给每个小句添加分隔符；
    splitstr=""
    for restr in tmpre:
        splitstr=splitstr+restr+";"
    # print(splitstr)

    content_seg = jieba.cut(splitstr)   # jieba分词
    # jieba.analyse.set_stop_words('ModifiedStopWord.txt')#设置停用词表
    # content_seg = tfidf(tmp_str) #使用TF-IDF算法进行分词
    # content_seg = jieba.analyse.textrank(splitstr) #使用Text-rank算法进行分词
    listcontent = ''
    for n in content_seg:
        listcontent +=n
        listcontent += " "
    # print(listcontent)
    listcontent_list=listcontent.split(" ")#将listcontent分隔成lsit以便去除停用词
    listcontent_last = movestopwords(listcontent_list)    # 去除停用词
    listcontent_last = listcontent_last.replace("   ", " ").replace("  ", " ")
    # print("".join(listcontent_last))
    savefile(fp, "".join(listcontent_last)) # 保存
fp.close()


# #对主题进行分割并保存
# for i in range(0,19999):
#     listcontent = str(df_train['theme-主题'][i])
#     if(listcontent=='nan'):
#         savefile(ft,"") # 保存
#         continue
#     listcontent = listcontent.replace(";", " ").replace("  ", " ")
#     print("".join(listcontent))
#     savefile(ft, "".join(listcontent)) # 保存
# ft.close()
