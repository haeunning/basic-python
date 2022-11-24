#참석자의 수를 사용자로부터 입력 받고 참석자에 맞추어서 준비해야 할 음식의 수를
#출력하는 프로그램을 작성해보자.
#치킨은 1인당 1마리, 맥주는 1인당 2캔, 케익은 1인당 4개씩 준비

number=int(input("참석자의 수를 입력하시오: "))
chickens=number
beers=number*2
cakes=number*4

print("준비해야 할 치킨의 수: ", chickens)
print("준비해야 할 맥주의 수: ", beers)
print("준비해야 할 케익의 수: ", cakes)

print("="*30)
#프로그래머라면, 이렇게 코딩한다.

nNumber=int(input("참석자의 수를 입력하시오: "))
nChickens=number*1
nBeers=number*2
fCakes=number*4.0

print("준비해야 할 치킨의 수: %d" %chickens)
print("준비해야 할 맥주의 수: %d" %beers)
print("준비해야 할 케익의 수: %d" %cakes)
