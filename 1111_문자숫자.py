#while문이 꼭 필요한 예제
#1부터 사용자가 입력한 정수 n까지 더해서 (1+2+3+...n)를 for 문을 이용하여 출력하

strSt = input("어디까지 더할까요? : ")

if ((strSt.isnumeric)==False) :
    print("문자입니다.")
else:
    print("숫자입니다.")
