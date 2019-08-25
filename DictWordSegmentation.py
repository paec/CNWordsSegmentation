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

with open('worddict.pickle', 'rb') as handle: #將pickle檔裡的set讀出
    worddict = pickle.load(handle)


def isEnglish(s):
    if s.islower() | s.isupper():
        return True
    
    return False

class StringBuilder:
     _file_str = None

     def __init__(self):
         self._file_str = StringIO()

     def Append(self, str):
         self._file_str.write(str)

     def __str__(self):
         return self._file_str.getvalue()

while True:

    try:
       
        # sentence = re.sub(r"["+zhon.hanzi.punctuation+string.punctuation+"]","",input("please input something: "))      
        sentence = "假如我們有抽取出這樣的entity，我們突然想要做判斷一篇新聞是不是負面新聞，是不是可以有很好的特徵去做分類訓練呢。"
        
        resultlist = list()
        length = len(sentence)

        start = 0 
        last = start+17 # dict裡最長的字串約為17
        count = 0

        while start!=length:

            count = count+1
            
            longword = sentence[start:last] 

                    
            if(isEnglish(longword[0])):

                sb = StringBuilder()

                tmpstart = start
                while tmpstart<len(sentence) and isEnglish(sentence[tmpstart]) :
                    sb.Append(sentence[tmpstart])
                    tmpstart = tmpstart+1

                resultlist.append(sb.__str__())
                start = tmpstart
                last = start+17 if start+17 < length else length

            elif start+1 == last :

                resultlist.append(longword)
                start = start + 1
                last = start+17 if start+17 < length else length
                # print(1)
            elif longword in worddict:

                resultlist.append(longword)
                start = last
                last = start+17 if start+17 < length else length
                # print(2)
            else:
                last = last -1
                # print(3)

        # print("\n")
        print(resultlist)
        # print("\n")
        print(count)

        break

    except EOFError:
        break








