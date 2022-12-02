n_data=[]
find_data=0

num=int(input("배수 입력 : "))
Max_num = int(input("최대값 입력 : "))
count=1

while (1):
    find_data = num * count
    if (find_data <= Max_num):
        n_data.append(find_data)
    else:
        break
    print(find_data)
    count = count+1
print(n_data)
