a=[12,34,45,67]
i=0
b=[]
while i<len(a):
    d=a[i]//10
    e=a[i]%10
    s=d+e
    b.append(s)
    i+=1
print(b)
