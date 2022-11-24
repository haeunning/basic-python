#두 정수의 합
# while 문을 이용하여서 입력한 두 정수의 합계를 반복해서 계산하는 프로그램을 작성해보자.

sum=0
data1 = 0
data2 = 0

while (1):
    data1=int(input("첫 번째 정수를 입력하시오: "))
    if (data1 != 0):
        data2 = int(input("두 번째 정수를 입력하시오: "))
        if (data2 !=0):
            sum = data1 + data2
            print("%d + %d = %d"%(data1, data2, sum))
        else:
            print("프로그램을 종료합니다.")
            break
    else:
        print("프로그램을 종료합니다.")
        break
