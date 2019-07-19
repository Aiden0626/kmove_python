a=1
alist=[1,2,3]

def add_data():
    a=2
    alist.append(4)
    print("안 %d" %a)
add_data()
print("바깥%d" %a)
print(alist)
print(type(alist))
print(type(a))