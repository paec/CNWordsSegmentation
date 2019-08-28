# -*- coding: utf-8 -*-
import pickle
import sys
import zhon
from zhon.hanzi import punctuation
import re 
from io import StringIO
import string

# -----------------------先將字典裡所有的詞，讀到set裡，並存成pickle檔-----------------------------
# with open("dict.txt","r" , encoding = "utf8") as f:
# 	worddict = set(f.read().splitlines())

# with open('worddict.pickle', 'wb') as handle:
#     pickle.dump(worddict, handle, protocol=pickle.HIGHEST_PROTOCOL)
# ------------------------------------------------------------------------------------------------

# with open('worddict.pickle', 'rb') as handle: #將pickle檔裡的set讀出
#     worddict = pickle.load(handle)

with open("welldict.txt","r" , encoding = "utf8") as f:
  worddict = set(f.read().splitlines())

maxlen = len(max(worddict,key=len))
start = int()
last = int()

def isnumoreng(s):
    if s.islower() or s.isupper() or s.isdigit():
        return True
    return False

def addtolist(num,word):
    global start
    global last
    resultlist.append(word)
    start = num
    last = start+maxlen if start+maxlen < length else length #字典裡最長詞長度約17


while True:

    try:

        # sentence = ""
        sentence = input()
        resultlist = list()
        length = len(sentence)
        start = 0 
        last = start+maxlen if start+maxlen < length else length

        while start!=length:
            
            if sentence[start]==" ": #略過空白
                start += 1
                continue
    
            if isnumoreng(sentence[start]): #如果是數字或英文開頭，直接掃到不是數字或英文為止，然後加入resultlist

                sb = str()
                tmpstart = start

                while tmpstart<length and isnumoreng(sentence[tmpstart]) :
                    sb += sentence[tmpstart]
                    tmpstart = tmpstart+1

                addtolist(tmpstart,sb)

                continue


            while True: #如果是中文字開頭，開始尋找匹配的詞

                longword = sentence[start:last] 
            
                if start+1 == last or longword in worddict:
                    addtolist(last,longword)
                    break
                else:
                    last = last -1


        print(resultlist)

        # break

    except EOFError:
        break








