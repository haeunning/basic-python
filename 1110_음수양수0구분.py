#음수,0,양수 구별

#if-elif-else
number = int(input("정수를 입력하시오: "))
if number<0:
    print("입력된 정수는 음수입니다.")
elif numbber ==0:
    print("입력된 정수는 0입니다.")
else:
    print("입력된 정수는 양수입니다.")

#중첩 if-else문
number = int(input("정수를 입력하시오: "))

if number<0:
    print("입력된 정수는 음수입니다.")
else:
    if number==0:
        print("입력된 정수는 0입니다.")
    else:
        print("입력된 정수는 양수입니다.")
