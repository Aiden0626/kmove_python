import random
for i in range(5):
    lotto = [0,0,0,0,0,0]
    for x in range(6):
        num=0
        while(num in lotto):
            num=random.randint(1,45)
        lotto[x]=num
    print("로또 : ",sorted(lotto)) 

# 로또2 중복은 못잡음
import random
for i in range(1,6):
    print("로또;",sorted(random.sample(range(1,46),6)))