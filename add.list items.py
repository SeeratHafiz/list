# list=[11,33,50]
# string=" "
# for i in list:
#     string=string+str(i)
# print(string)

list=[[2,4,3],[1,5,6],[9],[7,9,0]]
i=0
b=[]
while i<len(list):
    j=0
    while j<len(list[i]):
        b.append(list[i][j])
        j=j+1
    i=i+1
print(b)

# list=[[2,4,3],[1,5,6],[9],[7,9,0]]
# b=[]
# for i in list:
#     for j in i:
#         b.append(j)
# print(b)

