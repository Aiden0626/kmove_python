import time
input ("엔터후 20초")
start = time.time()
input("20초 후에 다시 엔터")
end = time.time()
et = end-start
print("실제시간 : ",et,"초")
print("차이:",abs(et-20),"초")#abs는 절대값