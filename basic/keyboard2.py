import random,time

n=1#문항수
w=["cat","dog","c","d","e","f","g","h","i"]
q=random.choice(w)
input('시작!')
start = time.time()
while n<=5:
    print("*문제",n)
    print(q)
    x=input()
    if q==x:
        print("통과!")
        n=n+1
        q=random.choice(w)
    else:
        print("오타!다시도전!")

end = time.time()
t=end-start
print('타자 시간 : {:.0f}초'.format(t))