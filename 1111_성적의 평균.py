#성적의 평균
# while문을 이용하여서 사용자로부터 음수를 입력받을 때까지 임의의 개수의 성적을 받아서
#평균을 계산한 후에 출력하는 프로그램을 작성하시오.

nGrade = 0

nSum = 0
nCount = 0
while (1):
    nGrade = int(input("성적을 입력하세요. : "))
    if (nGrade != -1):
        nSum = nSum + nGrade
        nCount = nCount + 1
    else:
        break

fAvg = nSum / nCount
print("%d 과목의 합은 %d이고, 평균은 %.2f 입니다." %(nCount, nSum, fAvg))

