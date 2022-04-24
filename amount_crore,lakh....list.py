a=[3000,600000,324990909,90990900,30000,560000,690909090,31010101,532010,5104100]
i=0
while i<len(a):
    if a[i]>=10000000:
        print(a[i],"crore")
    elif (a[i]>=100000):
        print(a[i],"lakh")
    else:
        print(a[i],"thousand")
    i=i+1