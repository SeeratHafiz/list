list=[[1,2,4],[2,4,4],[1,2]]
i=0
b=[]
while i<len(list):
    sum=0
    j=0
    while j<len(list[i]):
        sum+=list[j][i]
        j=j+1
    b.append(sum)
    i=i+1
print(b)