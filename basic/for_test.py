sum=0
for i in range(1,11):
    sum = sum + i
print(sum)

for i in range(2,10):
    for j in range(1,10):
        print("%d x %d = %d"%(i,j,i*j))
    print('')

for i in range(1,10):
    for j in range(2,10):
        print("%d x %d = %2d"%(j,i,i*j),end="  ")#%2d는 자리수 맟추기
    print('')