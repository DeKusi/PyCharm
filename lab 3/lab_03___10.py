text1 = open("text1.txt", "r")
st = text1.read(1)
st += text1.read()
#print("text1 :", st)
st = str(st)
st = st.replace(".", "")
st = st.replace(",", "")
st = st.replace("-", "")
st = st.lower()
lst = st.split()
textDict = {}
for i in range(0, len(lst)):
    x = lst[i]
    col = lst.count(lst[i])
    textDict[x]=col
#print(textDict)
textDict = str(textDict)
text2 = open("text2.txt", "w")
for s in textDict:
    text2.write(s)

#print("text1 :", st)
#print(lst)
#print(textDict)
text1.close()
