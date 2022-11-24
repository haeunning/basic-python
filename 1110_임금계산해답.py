#임금계산
#사용자로부터 근무시간과 시간당 임금을 입력받는다.
#주간 근무 시간이 40시간을  넘으면 초과 근무 시간에 대하여
#1.5배 임금을 지급해야한다고 하자.
#이번주에 받을 총 임금을 계산하는 프로그램을 작성하시오.

nWorkTime = int(input("근무 시간을 입력하시오.: "))
nPayPerHour = int(input("시간 당 임금을 입력하시오.: "))

if (nWorkTime > 40):
    nTotalPay = (40*nPayPerHour)+((nWorkTime-40)*(nPayPerHour*1.5))
else:
    nTotalPay = nWorkTime*nTotalPay

print("총 임금은 %d원 입니다."%nTotalPay)
