a=input("enter the number:")
l=len(a)
i=l-1
c=int(a)
b=[]
while i>=0:
    rev=c//(10**i)
    sum=rev*(10**i)
    c%=(10**i)
    print(sum,"+")
    i=i-1
    b.append(sum)
print(b)


# num=input("enter the number:")
# i=0
# add=""
# while i<len(num):
#     add+=num[i]
#     j=1
#     while j<len(num)-(i+1):
#         add+="0"
#         j+=1
#     if i==(len(num)-1):
#         break
#     else:
#         add+="+"
#     i+=1
# print(add)


    