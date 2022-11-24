#산술 연산 조건문을 사용한 홀짝 구분
n=int(input("Enter a number: "))
if n%2:
    print(n,"is odd.")
else:
    print(n,"is even.")


#같은 프로그램을 다른 코딩으로 구현
n=int(input("Enter a number: "))
s="even"
if n%2:
    s="odd"
print(n,"is",s)
