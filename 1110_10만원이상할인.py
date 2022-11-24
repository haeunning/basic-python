#인터넷 쇼핑몰에서 물건을 구입할 때, 구입액이 10만원 이상이면 5%의 할인을 해준다고 하자.
#사용자에게 구입 금액을 물어보고 최종적으로 할인 금액과 지분 금액을 출력하는 프로그램을 작성해보자.
total_sales = int(input("구입 금액을 입력하시오: "))
if total_sales >=100000 :
    discount = total_sales*0.05
    total_sales = total_sales-discount
print("지불 금액은", total_sales,"입니다.")
