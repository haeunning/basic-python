#1부터 사용자가 입력한 정수 n까지 더해서 (1+2+3+...n)를 for 문을 이용하여 출력하라
#for변수 in range() 구문을 사용

nEnd = int(input("어디까지 더할 까요?: "))

nSum=0
for i in range(0,nEnd+1,1):
    nSum = nSum+i

print("0에서부터 %d까지의 합은 %d입니다."%(nEnd,nSum))
