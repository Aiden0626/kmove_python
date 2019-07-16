# if문
money = True
if money:
    print("택시")
else:
    pass #구조상 뭔가 들어가야되기때문에 채워줌
    print("걸어감")
#print 줄을 맞춰야함, True를 False로 바꾸면 걸어감 뜸

#조건부표현식
jumsu= int(input("성적을 입력하세요"))
print('점수는 %a 입니다' %jumsu)
#format을 사용하는 방법도 있다(찾아보기)
print('입력한 성적은', jumsu,'점 입니다')#로 할수 있는건 다 문자여야 한다 하지만 지금은 위에 jumsu를 int해서 괜찮다

if jumsu >= 60:
    total = 'A'
elif  jumsu >= 80:
    total = 'B'
elif  jumsu >= 70:
    total = 'C'
elif  jumsu >= 60:
    total = 'D'
else:
    total='F'

print('당신의 학점은{}입니다.'.format(total))