

# list=[[0,1,2],[2,3,4],[3,4,5,6],[7,8,9,10,11],[12,13,14]]
# i=0
# n=[]
# while i<len(list):
#     sum=0
#     j=0
#     while j<1:
#         sum=sum+list[i][j]
#         j=j+1
#     n.append(sum) 
#     i=i+1
# print(n)


list=[2,3,1,5,10,7]
i=0
n=[]
while i<len(list):
    count=0
    j=i
    while j<len(list):
        if list[i]<list[j]:
            count=count+1
        j=j+1
    n.append(count)
    i=i+1
print(n)



# list=[1,0,3,4,5,7,0,9]
# n=[]
# i=0
# while i<len(list):
#     if list[i]!=0:
#         n.append(list[i])
#     i=i+1
# j=0
# while j<len(list):
#     if list[j]==0:
#         n.append(list[j])
#     j=j+1
# print(n)    