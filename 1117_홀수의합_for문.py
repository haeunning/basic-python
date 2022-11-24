#홀수의 합
#for문을 이용하여서 500과 1000사이에 있는 홀수의 합을 구하는 프로그램을 작성해보자
#187500

sum=0 #초기화필요
startNum = 500
endNum = 1000

for x in range(500,1001,1):
    if ((x%2)!=0):
        sum = sum + x
print("%d" %sum)
