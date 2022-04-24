print("welcome to KBC...........")
que=[["How many continents are there?"],["what is the capital of india"],["which course that NG will provide"]]
opt=[["four","nine","seven","nine"],["chandigarh","bhopal","chennai","delhi"],["software engineering","counselling","tourisam","agriculture"]]
sol=["seven","delhi","software engineering"]
i=0
c=0
while i<len(que):
    print(que[i])
    j=0
    while c<len(opt):
        while j<len(opt):
            c=c+1
            print(c,opt[i][j])
            j=j+1
    life1=input("u want life line")
    if life1=="yes":
        print("1.four","3.seven")
        ans1=input("select opt:")
        if ans1=="seven":
            print("correct")
            print("your answer is correct so you win Rs.10,000/-")
            print("you are qualified to the round")
            print("now the next question is:")
        break
    else:
        print("good")
        ans1=input("select opt:")
        if ans1=="seven":
            print("correct")
            print("your answer is correct so you win Rs.10,000/-")
            print("you are qualified to the round")
            print("now the next question is:")
        else:
            print("wrong")
            print("sorry! your answer is wrong so you are disqualified")
        break
i=i+1
c=0
while i<len(que):
    print(que[i])
    j=0
    while c<len(opt):
        while j<=len(opt):
            c=c+1
            print(c,opt[i][j])
            j=j+1
    life1=input("u want life line")
    if life1=="yes":
        print("1.chandigarh","4.delhi")
        ans2=input("select opt:")
        if ans2=="delhi":
            print("correct")
            print("your answer is correct so you win Rs.25,000/-")
            print("you are qualified to the round")
            print("now the next question is:")
        break
    else:
        print("great")
        ans2=input("select opt:")
        if ans2=="delhi":
            print("correct")
            print("your answer is correct so you win Rs.25,000/-")
            print("you are qualified to the round")
            print("now the next question is:")
        else:
            print("wrong")
            print("sorry! your answer is wrong so you are disqualified")
        break
i=i+1
c=0
while i<len(que):
    print(que[i])
    j=0
    while c<len(opt):
        while j<=len(opt):
            c=c+1
            print(c,opt[i][j])
            j=j+1
    life1=input("u want life line:")
    if life1=="yes":
        print("1.software engineering","4.agriculture")
        ans2=input("select opt:")
        if ans2=="software engineering":
            print("correct")
            print("congratulations!! your answer is correct so you win Rs.50,000/-")
        break
    else:
        print("great")
        ans2=input("select opt:")
        if ans2=="software engineering":
            print("correct")
            print("congratulations!! your answer is correct so you win Rs.50,000/-")
        else:
            print("wrong")
            print("sorry! your answer is wrong so you are disqualified")
        break

    









        
