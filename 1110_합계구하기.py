#while문을 사용하여 사용자가 입력한 시작값에서부터 종료값까지 더해서
#start_n+...+end_n을 계산하는 프로그램을 작성해보자.

sum=0
Start_Num = int(input("어디부터 더할 것인지 입력하시오.: "))
End_Num = int(input("어디까지 더할 것인지 입력하시오.: "))

nCount=Start_Num   #여기가 왕중요. 새 변수에 할당해주어야 밑에서 안꼬임.
while nCount <= End_Num:
    sum = sum+nCount
    nCount = nCount+1

print("%d부터 %d까지의 정수의 합 = %d"%(Start_Num,End_Num,sum))
