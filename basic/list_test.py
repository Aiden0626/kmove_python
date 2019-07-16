a=[]
b=[1,2,3]
c=['life','is']
d=[1,2,'life']
e=[1,2,[1,2,3]]

print(a)
print(b)
print(c)
print(d)
#print(e[3]) - 주석처리는 #

print(type('인간'))
print(e[2][1])

c=[1,2,3]
c[2]=4
print(c)

a=[1,2,3]
del a[1]
print(a)
a.append([5,6])
print(a)

b=[5,6,2,4,1]
b.sort()
print(b)
#튜플은 추가변경등 안되고 리스트는 가능

dic={1:10,2:{20}}
# {20}은 set 이라고 한다 값 자체를 구별하는것.
print(dic)

#없는건 추가 있는건 덮어씌움
a = {1: 'd'}
a[2] = 'e'
print(a)

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print ('name' in a)
print ('email' in a)
