def add(a,b):
    return a+b

print(add(5,4))
c=add(5,6)
print(c)

def add_many(choice,*a):
    result = 0
    print(type(a))
    print(a)
    for i in a:
        result=result+i
    return result

total = add_many(1,2,3,4,5,6,7,8,9,10)
print(total)
print()

def add_and_mul(a,b):
    return a+b,a*b

total = add_and_mul(3,6) #add,mul=add_and+mul(3,6)으로도 쓸 수 있음
add,mul = add_and_mul(3,6)
print(type(total))
print(type(add))
print(type(mul))
print(total)
print(add)
print(mul)

