import time,random
input('enter게임시작')
start = time.time()
count=0
oper=['+','-','*','/']
for x in range(0,5):
    a=random.randint(1,50)
    b=random.randint(1,50)
    op=random.choice(oper)

    quiz=str(a)+op+str(b)
    quiz='%d %s %d' %(a,op,b)

    print(quiz,'=')#문제출제
    
    print(eval(quiz))#답을 보여줌
    c=int(input('정답='))

    if int(eval(quiz))==c:
        print("정답!")
        count+=1
    else:
        print("오답")
end = time.time()
et = end-start
print("%.0f 초동안 %d개 맞음 "%(et,count))