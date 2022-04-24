#
#         i=i+1
print(a) i=0
a=[]
while i<len(a):
    j=0
    count=0# a=input("enter the alphabet:")

    while j<len(a):
        if a[i] in a:
            if a[i]==a[j]:
                count=count+1
                b.append(a[i])
                b.append(count)
            j=j+1

