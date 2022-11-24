#for문을 이용해서 1~100까지 더하는데 3의 배수만 건너뛰고 더하기

sum=0

for i in range(1,101,1):
    if i % 3==0:
        sum=sum+i

print("1~100까지의 합계(3의 배수 제외): ",sum)
