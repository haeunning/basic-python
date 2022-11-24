#초 단위의 시간을 입력받아서 몇 분 몇 초인지를 계산하는 프로그램을 작성해보자.

sec = int(input("초 단위 시간을 입력하세요.: "))
min = sec//60
remainder=sec%60

print("%d분 %d초"%(min, remainder))


#몇시몇분몇초
sec = int(input("초 단위 시간을 입력하세요.: "))
hour=sec//3600
sec=sec-(hour*3600)
min=sec//60
reamainder=sec%60
print("%d시간 %d분 %d초"%(hour, min, remainder))
