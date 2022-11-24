#전화번호를 포함한 문자열에서 뒤의 4자리 번호만 추출하려면?
phonenum = '010-1234-5678'
last4num = phonenum[9]+phonenum[10]+phonenum[11]+phonenum[12]
print(last4num)

#4개의 전화번호를 한번에 추출할 수 없을까?
phonenum = '010-1234-2543'
last4num = phonenum[9:13]
print(last4num)
