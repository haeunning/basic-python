def get_sum(start, end):
    sum=0
    for i in range(start, end+1):
        sum = sum+i
    return sum

sum1 = get_sum(1,10)
sum2 = get_sum(1,100)

print(sum1, sum2)
