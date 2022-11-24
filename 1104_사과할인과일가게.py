#연세 과일가게에서 사과를 1개에 1000원, 배 1개에 2000원,
#멜론은 1개에 3000원에 판매하고 있다. 그런데 오늘은 사과가 시들어서
#원래 가격의 10%를 할인해서 팔려고 한다. 고객들이 구매한 과일 총액을
#계산하여 정수로 출력하는 프로그램을 작성해보자.

apple=int(input("사과 갯수를 입력하세요: "))
apple_rate=float(input("오늘 사과의 sale %를 입략하세요:"))

pear=int(input("배 갯수를 입력하세요: "))
melon=int(input("멜론 갯수를 입력하세요: "))

apple_total=apple*(1000-((apple_rate/100)*1000))
pear_total=pear*2000
melon_total=melon*3000

total=apple_total+pear_total+melon_total
total=int(total)

print("전체 금액은: %d" %total)
print("전체 금액은: %d,%03d" %(total//1000,total%1000))
