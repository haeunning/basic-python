#누적합계가 1000이상이 되는 시작 시점 해답

sum=0
for i in range(1,101):
    sum = sum+i
    if sum >= 1000:
        break
print("1~100의 합에서 최초로 1000이 넘는 위치: %s"%i)
