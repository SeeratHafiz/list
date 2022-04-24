# list=[1,1,2,3,4,1]
# a=[]
# b=0
# for i in range(len(list)):
#     if list[i]!=1:
#         a.append(list[i])
# print(a)


list1=[10,20,10,20,11,13]
newlist=[]
i=0
while i<len(list1):
    j=0
    count=0
    while j<len(list1):
        if list1[i]==list1[j]:
            count+=1
            a=list1[i]
        j=j+1
    i=i+1
    if count>2 or count<2:
        if a not in newlist:
            newlist.append(a)
print(newlist)



