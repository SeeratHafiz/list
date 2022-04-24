a=[4,6,4,3,3,4,3,4,3,8]
b=[]
i=0
c=3
count=0
while i<len(a):
    if a[i]==c:
        count=count+1
    i=i+1
b.append(count)
b.append(c)
print(b)                       

