#인터넷 뱅킹을 사용하다 보면 계좌번호를 입력할 때, "312-01-1234567"과 같이 "-"을 사용하면 안된다는 경고를 받는다
#사용자로부터 "-"가 포함된 계좌번호를 받아서 "-"을 삭제한 문자열을 만들어보자.

#interable object(sequence에 사용) 반복 가능한 객체
#파이썬에서 for 루프와 함께 사용할 수 있는 객체

raw = input("계좌번호를 입력하시오.: ")
processed=""
for c in raw:
    if c!="-":
        processed=processed+c
print(processed)
