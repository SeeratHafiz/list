a=["1","2","3","4","5","6"]
i=0
b=[]
c=[]
d=0
while i<len(a)-1:
    d=str(a[i]+str(a[i+1]))
    c.append(d)
    i+=1
print(c)
