#합계 구하기
#1부터 사용자가 입력한 정수 n까지 더해서 (1+2+3+...n)을 계산하는 프로그램을 작성해보자
#for변수 in range() 구문을 사용
nStart = int(input("어디서부터 더할까요? : "))
nEnd = int(input("어디까지 더할까요? : "))

nSum = 0

for i in range(nStart,nEnd+1,1):
    nSum = nSum+i

print("%d에서부터 %d까지의 합은 %d입니다."%(nStart,nEnd,nSum))
