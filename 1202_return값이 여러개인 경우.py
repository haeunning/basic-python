#반환값이 여러개인 경우
def add_multiply(x,y):
    sum = x+y
    mult = x*y
    return sum, mult #튜플로 반환

#main
a = int(input('Enter a : '))
b = int(input('Enter b : '))
m,n = add_multiply(a,b)
print(m,n)
