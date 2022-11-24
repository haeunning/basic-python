sum=0
Start_Str = input("어디부터 더할 것인지 입력하시오: ")
while(Start_Str.isnumeric()==False):
    Start_Str = input("어디부터 더할지 숫자만 입력하시오: ")
Start_Num = int(Start_Str)

End_Str = input("어디까지 더할 것인지 입력하시오: ")
while (End_Str.isnumeric()==False):
    End_Str = input("어디까지 더할 것인지 입력하시오: ")
End_Str = int(End_Str)

while Start_Num <= End_Str:
    sum = sum + Start_Num
    Start_Num = Start_Num+1
print("%s부터 %s까지 정수의 합 = %d"%(Start_Num,End_Str, sum))
