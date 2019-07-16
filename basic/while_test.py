listdata=[]
while True: #while 문은 들여쓰기,전체드래그후 탭)
    print('''
    =====================리스트 데이터 관리=====================
    1. 리스트 추가 2.리스트 데이터 수정 3.리스트 데이터 삭제 4.종료
    ''')
    menu = int(input("메뉴를 선택해라")) #숫자일경우  input 앞에 int

    if menu == 4 :
        break
    elif menu == 1 :
        data=input("추가할 데이터를 입력하세요")
        listdata.append(data)
        print(listdata)
    elif menu == 2 :
        data=input("수정할 데이터를 입력하세요")
        a=int(input("몇번째 데이터?"))
        listdata[a-1]=data
        print(listdata)
    elif menu == 3 :
        a=int(input("몇번째 데이터?"))
        del listdata[a-1]
        print(listdata)
        