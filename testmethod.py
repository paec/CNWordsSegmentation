
with open("16萬詞典.txt","r" , encoding = "utf8") as f:
  worddict = f.read().splitlines()


print(type(worddict))
print(len(worddict))
worddict.sort(key = len,reverse = True)

sentence = "他今年17歲"
used = set()

for word in worddict :

    if word in used :
        continue

    if sentence.find(word) > -1:
        sentence = sentence.replace(word," "+word+" ")

        used.add(word)

        for w in word:
            used.add(w)


print(sentence.strip())


