#숫자세기
#while문을 이용하여 양의 정수 a,b를 입력받아 a부터 b까지 출력하는 프로그램을 작성해보자(단, a<=b)


a=int(input("a를 입력하시오: "))
b=int(input("b를 입력하시오: "))

i=a
while (i<=b):
    print("Count",i)
    i +=1
