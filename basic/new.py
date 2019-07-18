import random,time

n=1#문항수
w=["cat","dog","c","d","e","f","g","h","i"]
rank={}
start = time.time()
def sortV(x):
    return x[1]#(k:v)중에 v값으로 정렬한다
while True :
    print("1.문제불러오기 2.타자게임")
    menu = input("메뉴를 선택해\n")
    if menu=='1':
        f=open('basic/word.txt','r')
        line=1
        w.clear()
        while line:
            line = f.readline().replace("\n","")
            if not(line==''):
                w.append(line)
        print(w)
    elif menu=='2':
        n=1
        print("[타자게임]준비되면 엔터")
        input()
        start = time.time()
        q=random.choice(w)
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
        t=format(t,".2f")
        print("타자 시간 : ",t,"초")
        name = input("사용자 이름을 입력하세요")
        rank[name]=float(t)
    elif menu=='3':
        ranklist=sorted(rank.items(),key=sortV)
        num=1
        for k,v in ranklist:
            print("%d등 %s %f" %(num,k,v))
            num=num+1
    elif menu=='4':
        f=open('rank.txt','w')
        text=''
        items=rank.items()
        for k,v in items:
            text=text+k+':'+str(v)+'\n'
        f.writelines(text)
        f.close()
    elif menu=='5':
        f=open('rank.txt','r')
        line=1
        while line:
            line = f.readline().replace("\n","")
            if not(line==''):
                k,v=line.split(':')
                rank[k]=float(v)
    else:
        print("메뉴미스")
end = time.time()
t=end-start
print('타자 시간 : {:.0f}초'.format(t))