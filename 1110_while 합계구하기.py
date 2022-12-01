#while:조건이 만족되는 동안 반복
#for:정해진 횟수만큼 반복

#합계구하기

#while문을 사용하여 1부터 사용자가 입력한 정수 n까지 더해서 합을 계산하는 프로그램을 작성해보자.

i=1 #조건식에 사용할 변수를 1로 초기화
sum=0 #초기화 필요
limit=int(input("어디까지 더할 것인지 입력하시오: "))

while i<=limit:
    sum=sum+i
    i=i+1
print(limit, "까지의 정수의 합=", sum)

print(' ')
print("="*30)
print(' ')
print('[문자열 포맷팅]')

#문자열 포맷팅
i=1 #조건식에 사용할 변수를 1로 초기화
sum=0 #초기화 필요
limit=int(input("어디까지 더할 것인지 입력하시오: "))

while i<=limit:
    sum=sum+i
    i=i+1
print("1부터 %d까지의 정수의 합= %d"%(limit, sum))
