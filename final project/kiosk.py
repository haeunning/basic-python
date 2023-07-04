###############################################################################################################################
########################################################## 함수 생성 ##########################################################
###############################################################################################################################

### 첫 화면
def customer_cnt():
    global customer
    print("============================================================")
    print("안녕하세요 오늘 저희 매장을 방문해주신 {}번째 손님이십니다♥".format(customer))
    print("============================================================")
    customer = customer + 1


### 매장 or 포장
def in_or_out():
    print(inout)
    print()
    in_out = int(input('주문 방식의 번호를 선택해주세요 : '))
    if in_out == 1:
        print("음료가 다회용컵에 제공됩니다")
    elif in_out == 2:
        print("음료가 일회용컵에 제공됩니다")
    print('---------------------------------------------')


### 주문 대범주
def choose_category():
    global cat
    print(category)
    print()
    cat = int(input('주문하실 메뉴의 카테고리 번호를 선택해주세요 : '))
    print('---------------------------------------------')


### 커피 주문
def order_coffee():
    global coffee, cnt, ice, total_price, price, basket
    print('▒커피(Coffee)▒')
    for item in coffee_menu:
        print("{} :".format(item), format(coffee_menu[item], ',') + "원")
    print()
    print('※ 기본은 Hot입니다. Ice 옵션 선택 시 300원이 추가됩니다.')
    print('※ 기본은 Regular입니다. Large 옵션 선택 시 500원이 추가됩니다.')
    print()
    coffee = int(input('주문하실 메뉴의 번호를 선택해주세요 : '))
    ice = int(input('Ice 옵션 선택을 원하시면 1을, 아니면 2를 선택해주세요 : '))
    size = int(input('Large 옵션 선택을 원하시면 1을, 아니면 2를 선택해주세요 : '))
    cnt = int(input('구입하실 수량을 선택해주세요 : '))
    if coffee in [i for i in range(1, len(coffee_menu) + 1)]:
        if ice == 1:
            if size == 1:
                total_price = total_price + (coffee_menu[list(coffee_menu)[coffee - 1]] + 800) * cnt
                for _ in range(cnt):
                    basket.append("{}(Ice) L".format(list(coffee_menu)[coffee - 1]))
                price.append(coffee_menu[list(coffee_menu)[coffee - 1]] + 800)
            elif size == 2:
                total_price = total_price + (coffee_menu[list(coffee_menu)[coffee - 1]] + 300) * cnt
                for _ in range(cnt):
                    basket.append("{}(Ice)".format(list(coffee_menu)[coffee - 1]))
                price.append(coffee_menu[list(coffee_menu)[coffee - 1]] + 300)
        elif ice == 2:
            if size == 1:
                total_price = total_price + (coffee_menu[list(coffee_menu)[coffee - 1]] + 500) * cnt
                for _ in range(cnt):
                    basket.append("{}(Hot) L".format(list(coffee_menu)[coffee - 1]))
                price.append(coffee_menu[list(coffee_menu)[coffee - 1]] + 500)
            elif size == 2:
                total_price = total_price + (coffee_menu[list(coffee_menu)[coffee - 1]] * cnt)
                for _ in range(cnt):
                    basket.append("{}(Hot)".format(list(coffee_menu)[coffee - 1]))
                price.append(coffee_menu[list(coffee_menu)[coffee - 1]])


### 라떼 주문
def order_latte():
    global latte, cnt, ice, total_price, price, basket
    print('▒라떼(Latte)▒')
    for item in latte_menu:
        print("{} :".format(item), format(latte_menu[item], ',') + "원")
    print()
    print('※ 기본은 Hot입니다. Ice 옵션 선택 시 300원이 추가됩니다.')
    print('※ 기본은 Regular입니다. Large 옵션 선택 시 500원이 추가됩니다.')
    print()
    latte = int(input('주문하실 메뉴의 번호를 선택해주세요 : '))
    if latte != 4:
        ice = int(input('Ice 옵션 선택을 원하시면 1을, 아니면 2를 선택해주세요 : '))
        size = int(input('Large 옵션 선택을 원하시면 1을, 아니면 2를 선택해주세요 : '))
        cnt = int(input('구입하실 수량을 선택해주세요 : '))
        if latte in [i for i in range(1, len(latte_menu) + 1)]:
            if ice == 1:
                if size == 1:
                    total_price = total_price + (latte_menu[list(latte_menu)[latte - 1]] + 800) * cnt
                    for _ in range(cnt):
                        basket.append("{}(Ice) L".format(list(latte_menu)[latte - 1]))
                    price.append(latte_menu[list(latte_menu)[latte - 1]] + 800)
                elif size == 2:
                    total_price = total_price + (latte_menu[list(latte_menu)[latte - 1]] + 300) * cnt
                    for _ in range(cnt):
                        basket.append("{}(Ice)".format(list(latte_menu)[latte - 1]))
                    price.append(latte_menu[list(latte_menu)[latte - 1]] + 300)
            elif ice == 2:
                if size == 1:
                    total_price = total_price + (latte_menu[list(latte_menu)[latte - 1]] + 500) * cnt
                    for _ in range(cnt):
                        basket.append("{}(Hot) L".format(list(latte_menu)[latte - 1]))
                    price.append(latte_menu[list(latte_menu)[latte - 1]] + 500)
                elif size == 2:
                    total_price = total_price + (latte_menu[list(latte_menu)[latte - 1]] * cnt)
                    for _ in range(cnt):
                        basket.append("{}(Hot)".format(list(latte_menu)[latte - 1]))
                    price.append(latte_menu[list(latte_menu)[latte - 1]])
    elif latte == 4:
        print("해당 메뉴는 Ice만 가능한 메뉴입니다(Ice 추가금 300원이 포함된 가격입니다)")
        size = int(input('Large 옵션 선택을 원하시면 1을, 아니면 2를 선택해주세요 : '))
        cnt = int(input('구입하실 수량을 선택해주세요 : '))

        if size == 1:
            total_price = total_price + (latte_menu[list(latte_menu)[latte - 1]] + 500) * cnt
            for _ in range(cnt):
                basket.append("{}(Ice) L".format(list(latte_menu)[latte - 1]))
            price.append(latte_menu[list(latte_menu)[latte - 1]] + 500)
        elif size == 2:
            total_price = total_price + (latte_menu[list(latte_menu)[latte - 1]]) * cnt
            for _ in range(cnt):
                basket.append("{}(Ice)".format(list(latte_menu)[latte - 1]))
            price.append(latte_menu[list(latte_menu)[latte - 1]])


### 티 주문
def order_tea():
    global tea, cnt, ice, total_price, price, basket
    print('▒티(Tea)▒')
    for item in tea_menu:
        print("{} :".format(item), format(tea_menu[item], ',') + "원")
    print()
    print('※ 기본은 Hot입니다. Ice 옵션 선택 시 300원이 추가됩니다.')
    print('※ 기본은 Regular입니다. Large 옵션 선택 시 500원이 추가됩니다.')
    print()
    tea = int(input('주문하실 메뉴의 번호를 선택해주세요 : '))
    ice = int(input('Ice 옵션 선택을 원하시면 1을, 아니면 2를 선택해주세요 : '))
    size = int(input('Large 옵션 선택을 원하시면 1을, 아니면 2를 선택해주세요 : '))
    cnt = int(input('구입하실 수량을 선택해주세요 : '))
    if tea in [i for i in range(1, len(tea_menu) + 1)]:
        if ice == 1:
            if size == 1:
                total_price = total_price + (tea_menu[list(tea_menu)[tea - 1]] + 800) * cnt
                for _ in range(cnt):
                    basket.append("{}(Ice) L".format(list(tea_menu)[tea - 1]))
                price.append(tea_menu[list(tea_menu)[tea - 1]] + 800)
            elif size == 2:
                total_price = total_price + (tea_menu[list(tea_menu)[tea - 1]] + 300) * cnt
                for _ in range(cnt):
                    basket.append("{}(Ice)".format(list(tea_menu)[tea - 1]))
                price.append(tea_menu[list(tea_menu)[tea - 1]] + 300)
        elif ice == 2:
            if size == 1:
                total_price = total_price + (tea_menu[list(tea_menu)[tea - 1]] + 500) * cnt
                for _ in range(cnt):
                    basket.append("{}(Hot) L".format(list(tea_menu)[tea - 1]))
                price.append(tea_menu[list(tea_menu)[tea - 1]] + 500)
            elif size == 2:
                total_price = total_price + (tea_menu[list(tea_menu)[tea - 1]] * cnt)
                for _ in range(cnt):
                    basket.append("{}(Hot)".format(list(tea_menu)[tea - 1]))
                price.append(tea_menu[list(tea_menu)[tea - 1]])


### 주스 주문
def order_juice():
    global juice, cnt, ice, total_price, price, basket
    print('▒주스(Juice)▒')
    for item in juice_menu:
        print("{} :".format(item), format(juice_menu[item], ',') + "원")
    print()
    print("주스는 Ice만 가능합니다(Ice 추가금 300원이 포함된 가격입니다)")
    print('※ 기본은 Regular입니다. Large 옵션 선택 시 500원이 추가됩니다.')
    print()
    juice = int(input('주문하실 메뉴의 번호를 선택해주세요 : '))
    size = int(input('Large 옵션 선택을 원하시면 1을, 아니면 2를 선택해주세요 : '))
    cnt = int(input('구입하실 수량을 선택해주세요 : '))
    if juice in [i for i in range(1, len(juice_menu) + 1)]:
        if size == 1:
            total_price = total_price + (juice_menu[list(juice_menu)[juice - 1]] + 500) * cnt
            for _ in range(cnt):
                basket.append("{}(Ice) L".format(list(juice_menu)[juice - 1]))
            price.append(juice_menu[list(juice_menu)[juice - 1]] + 500)
        elif size == 2:
            total_price = total_price + (juice_menu[list(juice_menu)[juice - 1]] * cnt)
            for _ in range(cnt):
                basket.append("{}(Ice)".format(list(juice_menu)[juice - 1]))
            price.append(juice_menu[list(juice_menu)[juice - 1]])


### 주문 종료 or 추가 주문
def end_or_keep():
    while True:
        global end
        end = int(input('주문을 마치시려면 1을, 추가 주문을 원하시면 2를 선택해주세요 : '))
        print()
        if end not in [1, 2]:
            print("오류! 번호를 다시 선택해주세요")
            continue
        elif end == 1:
            break
        break


### 주문 내역 확인
def check_order():
    global basket2, cnt2, price, total_price
    print('주문하신 음료를 확인해주세요')
    print()
    print('****************주문 내역*****************')
    basket2 = []
    cnt2 = []
    for m in basket:
        if m not in basket2:
            basket2.append(m)
    for n in basket2:
        cnt2.append(basket.count(n))
    print("상품명           수량     금액")
    for h in range(len(basket2)):
        print("{}     {}     {}".format(basket2[h][2:], cnt2[h], price[h] * cnt2[h]))
    print('-----------------------------------------')
    print("결제하실 총 금액은", format(total_price, ',') + "원입니다")
    print('*****************************************')
    print()


def receipt_or_not():
    if receipt == 1:
        print()
        print("영수증이 발급됩니다")
        print()
        print('****************영수증*****************')
        print('------------♥Yonsei Cafe♥------------')
        print('--------------주문 번호 {}--------------'.format(order_cnt))
        print('---------------------------------------')
        print("상품명           수량     금액")
        for h in range(len(basket2)):
            print("{}     {}     {}".format(basket2[h][2:], cnt2[h], price[h] * cnt2[h]))
        print('---------------------------------------')
        print("결제하신 총 금액은", format(total_price, ',') + "원입니다")
        print('***************************************')
        print()


### 결제 or 수정 or 취소
def buy_or_not():
    global price, total_price, new_total_price, basket2, cnt2, order_cnt, receipt
    buy = int(input('결제를 진행하시려면 1을, 수정하시려면 2를, 취소하시려면 3을 선택해주세요 : '))
    print()
    if buy == 1:
        receipt = int(input("영수증을 발급 받으시려면 1을, 아니면 2를 선택해주세요 : "))
        print()
        print("카드를 투입구에 넣어주세요")
        print("결제 중입니다 잠시만 기다려주세요")
        for i in range(10):
            print('.')
        print("결제가 완료되었습니다")
        receipt_or_not()
        print("감사합니다♥")
        order_cnt = order_cnt + 1
        print()
        print()
        print()
    elif buy == 2:
        plus_minus = int(input("추가 주문을 하시려면 1을, 담으신 상품 제거를 하시려면 2를 선택해주세요 : "))
        print()
        if plus_minus == 1:
            while True:
                # 주문 대범주 선택
                choose_category()
                # 커피 주문
                if cat == 1:
                    order_coffee()
                    end_or_keep()
                    if end == 2:
                        continue
                    break
                # 라떼 주문
                elif cat == 2:
                    order_latte()
                    end_or_keep()
                    if end == 2:
                        continue
                    break

            # 주문내역 확인
            check_order()
            print()
            receipt = int(input("영수증을 발급 받으시려면 1을, 아니면 2를 선택해주세요 : "))
            print()
            print("카드를 투입구에 넣어주세요")
            print("결제 중입니다 잠시만 기다려주세요")
            for i in range(10):
                print('.')
            print("결제가 완료되었습니다")
            receipt_or_not()
            print("감사합니다♥")
            order_cnt = order_cnt + 1
            print()
            print()
            print()

        elif plus_minus == 2:
            while True:
                print("상품번호     상품명           수량")
                for h in range(len(basket2)):
                    print("{}       {}     {}".format(h + 1, basket2[h][2:], cnt2[h]))
                print()
                a = int(input("제거하고자 하는 상품의 번호를 입력해주세요 : "))
                b = int(input("제거하고자 하는 수량을 입력해주세요 : "))
                c = cnt2[a - 1]

                cnt2[a - 1] = cnt2[a - 1] - b

                print()
                if cnt2[a - 1] < 0:
                    print("오류! 기존 주문량인 {}보다 많은 수량을 제거하셨습니다".format(c))
                    print("수량이 0으로 변경됩니다")
                    cnt2[a - 1] = 0
                print()
                d = int(input("계속 제거를 원하시면 1을, 결제를 원하시면 2를 선택해주세요 : "))
                print()
                if d == 2:
                    break

            print('주문하신 음료를 확인해주세요')
            print()
            print('****************주문 내역*****************')
            print("상품명           수량     금액")
            total_price = 0
            for h in range(len(basket2)):
                print("{}     {}     {}".format(basket2[h][2:], cnt2[h], price[h] * cnt2[h]))
                total_price = total_price + (price[h] * cnt2[h])
            print('-----------------------------------------')
            print("결제하실 총 금액은", format(total_price, ',') + "원입니다")
            print('*****************************************')
            print()
            receipt = int(input("영수증을 발급 받으시려면 1을, 아니면 2를 선택해주세요 : "))
            print()
            print("카드를 투입구에 넣어주세요")
            print("결제 중입니다 잠시만 기다려주세요")
            for i in range(10):
                print('.')
            print("결제가 완료되었습니다")
            receipt_or_not()
            print("감사합니다♥")
            order_cnt = order_cnt + 1
            print()
            print()
            print()

    elif buy == 3:
        print("주문이 취소되었습니다")
        print()
        print()
        print()
        basket = []
        basket2 = []
        cnt2 = []
        price = []
        total_price = 0
    print()





###############################################################################################################################
########################################################## 구현 코드 ##########################################################
###############################################################################################################################

customer = 1
order_cnt = 1
inout = '▒주문 방식▒\n1.매장(For Here) | 2.포장(Take-out)'
category = '▒카테고리▒\n1.커피(Coffee) | 2.라떼(Latte) | 3.티(Tea) | 4.쥬스(Juice)'
coffee_menu = {"1.에스프레소": 1900, "2.아메리카노": 2600, "3.디카페인 아메리카노": 3100, "4.헤이즐넛 아메리카노": 3000, "5.카페모카": 4000, "6.카라멜 마끼야또": 4000}
latte_menu = {"1.초코라떼": 3700, "2.녹차라떼": 3700, "3.토피넛라떼": 4000, "4.딸기라떼": 4000}
tea_menu = {"1.유자차": 3500, "2.자몽차": 3900, "3.레몬차": 3900, "4.얼그레이": 3700, "5.캐모마일": 3700}
juice_menu = {"1.딸기주스": 4000, "2.망고주스": 4100, "3.블루베리주스": 4300, "4.수박주스": 4300}

while True:
    # 기본 세팅
    total_price = 0
    basket = []
    price = []

    # 첫 화면
    customer_cnt()
    print()
    # 매장 or 포장
    in_or_out()

    while True:
        # 주문 대범주 선택
        choose_category()

        # 커피 주문
        if cat == 1:
            order_coffee()
            end_or_keep()
            if end == 2:
                continue
            break

        # 라떼 주문
        if cat == 2:
            order_latte()
            end_or_keep()
            if end == 2:
                continue
            break

        # 티 주문
        if cat == 3:
            order_tea()
            end_or_keep()
            if end == 2:
                continue
            break

        # 주스 주문
        if cat == 4:
            order_juice()
            end_or_keep()
            if end == 2:
                continue
            break

    # 주문내역 확인
    check_order()

    # 결제 or 수정 or 취소
    buy_or_not()


# 주문완료 (손님용)
# 시스템종료 (직원용) -> 하루 총 주문 고객 수, 매출 등 확인 가능


# 휘핑크림 -> 라떼에만
# 샷추가는 모든 음료 옵션
# 커피, 라떼, 티(아이스티)에는 샷추가
# 얼음 (많이 적게 보통)
# 결제금액이 총 0원인 경우, 종료.
