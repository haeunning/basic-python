#학생들의 성적을 받아서 성적이 90점 이상이면 A학점, 80점 이상이고 90점 미만이면 B학점,
# 70점이상이고 80점 미만이면 C학점, 60점 이상이고 70점 미만이면 D학점, 60점 미만이면 F 학점 출력

#if-elif-else
score = int(input("정수를 입력하세요.: "))

if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")
print("학점입니다.")

#중첩 if-else문
score = int(input("정수를 입력하세요.: "))

if score>=90:
    print("A")
else:
    if 80<=score:
        print("B")
    else:
        if 70<=score:
            print("C")
        else:
            if 60<=score:
                print("D")
            else:
                print("F")
print("학점입니다.")
