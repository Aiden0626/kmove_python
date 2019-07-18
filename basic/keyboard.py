import random
import time

n=1
num1='가'
num2='나'
num3='다'
num4='라'
num5='마'
com=random.choice(num1,num2,num3,num4,num5)
input("시작")
start = time.time()
while n<=5:
    print("*문제",n)
    print(com)
    x=input()
    if com==x:
        print("통과")
        n=n+1
        com=random.choice(num1,num2,num3,num4,num5)

end = time.time()
t=end-start
print('타자 시간 : {:.0f}초'.format(t))