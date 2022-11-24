#변수 x와 변수y의 값을 입력받은 후 서로 값을 바꾸는 프로그램을 작성해보자.
x=int(input("x를 입력하시오: "))
y=int(input("y를 입력하시오: "))
print("교환 전 = x:",x,"y:", y)

temp=x
x=y
y=temp

print("교환 후 = x:",x,"y:",y)
