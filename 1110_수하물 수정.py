#수하물비용계산
#A항공사에서는 수하물을 부칠때 20kg이 넘어가면 수하물에 대한 수수료로 20,000원을 지불해야한다.

fWeight = float(input("수하물의 무게는 얼마입니까? : "))
if fWeight > 40:
    print("탑재 중량 초과입니다.")
    if fWeight>20:
        print("무거운 수하물은 20,000원을 내셔야 합니다.")
else:
    print("수하물에 대한 수수료는 없습니다.")
print("감사합니다")
