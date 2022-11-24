#연세마트에서 사과가 신선하면 사과를 사기로 한다. 만약 사과가 개당 1000원 미만이면
#10개를 산다. 하지만 사과가 개당 1000원 이상이면 5개만 산다.

strAppleQuality = input("사과의 상태를 입력하시오: ")

if strAppleQuality=="신선":
    nApplePrice = int(input("사과 1개의 가격을 입력하시오. : "))
    if nApplePrice<1000:
        print("10개를 산다.")
    else:
        print("5개를 산다.")
else:
    print("사과를 사지 않는다.")
