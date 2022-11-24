#사용자로부터 신장과 체중을 입력받아서 BMI값을 출력하는 프로그램을 작성해보자.
fWeight=float(input("몸무게를 kg 단위로 입력하시오.: "))
fHeight=float(input("키를 미터 단위로 입력하시오.: "))

fBmi=(fWeight/(fHeight**2))
print("당신의 BMI=%.2f"%(fBmi))
