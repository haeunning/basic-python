def print_sum(*nums, sumfmt = "Sun is %d"): #nums는 튜플 변수로 정의됨
    sum=0
    for n in nums:
         sum = sum+n
    print(sumfmt %sum)

print_sum()
print_sum(1,2,3,4,5)
print_sum(1,2,3,4,5, sumfmt = "전체 합은 %d입니다.")
