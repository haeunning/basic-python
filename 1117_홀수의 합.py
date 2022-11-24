#홀수의 합
#for문을 이용하여서 500과 1000사이에 있는 홀수의 합을 구하는 프로그램을 작성해보자
#187500

sum=0 #초기화필요
startNum = 500
endNum = 1000
while (1):
    if ((startNum %2)!=0):
        sum = sum + startNum
    if (startNum >= endNum):
        break
    startNum = startNum+1
print("%d" %sum)
