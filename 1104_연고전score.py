#사용자에게 경기장, 이긴 팀, 진 팀, 우수 선수, 스코어를 질문하고 변수에 저장한다. 
#이들 문자열에 문장을 붙여서 기사를 작성하는 프로그램을 작성하자.

stadium = input("경기장은 어디입니까? ")
winner = input("이긴 팀은 어디입니까? ")
loser = input("진 팀은 어디입니까? ")
vip = input("우수 선수는 누구입니까? ")
score = input("스코어는 몇 대 몇입니까? ")

print("")
print("="*30)

#변수와 문자열을 연결하여 기사를 작성한다.
print("오늘", stadium,"에서 연고전 경기가 열렸습니다.")
print(winner, "와", loser, "는 치열한 공방전을 펼쳤습니다.")
print(vip, "이(가) 맹활약을 하였습니다.")
print("결국", winner, "가", loser, "를", score, "로 이겼습니다.")

print("="*30)
print("")
print("="*30)

print("오늘 %s에서 연고전 경기가 열렸습니다." %stadium)
print("%s와 %s는 치열한 공방전을 펼쳤습니다." %(winner, loser))
print(vip, "이(가) 맹활약을 하였습니다.")
print("결국", winner, "가", loser, "를", score, "로 이겼습니다.")

print("="*30)
