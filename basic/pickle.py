import pickle


w=[]
rank
    
while True:
    print("1문제열기2문제저장3타자게임4등수목록5.저장")
    munu=input("메뉴를 선택하세요\n")
    if menu=='1':
        f=open('word_p.txt','rb')
        w=w+pickle.load(f)
        f.close()
    elif menu=='2':
        f=open('word_p.txt','wb')
        pickle.dump(w,f)
        f.close()
    elif menu=='7':
        word=input("answpdlqfur")
        w.append(word)
    elif menu=='3':
        n=1
        print("[타자게임]준비되면 엔터")
data={1:'python',2:'you'}
f=open('test_p.txt','wb')
pickle.dump(data,f)
f.close()

f=open('test_p.txt','rb')
data1=pickle.load(f)
f.close

print(data)
print(data1)
print(type(data1))