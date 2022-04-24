list=["a","b","c","d","e","f","g","h"]
a=[]
b=[]
i=0
while i<len(list):
    if i<3:
        a.append(list[i])
    else:
        b.append(list[i])
    i=i+1
b.append(a)
print(b)