total_sales = int(input("구입 금액을 입력하시오.: "))
if total_sales >= 100000:
    discount = total_sales*0.05
    total_sales = total_sales - discount

print("지불 금액은 %.0f 입니다."%total_sales)
