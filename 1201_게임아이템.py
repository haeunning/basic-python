#딕셔너리를 생성합니다.
character = {
    "name":"기사",
    "level":12,
    "items":{
        "sword":"불꽃의 검",
        "armor":"풀플레이트",
        },
    "skill":["베기","세게 베기","아주 세게 베기"]}

for key in character:
    if type(character[key]) is str:
        print(key, ":", character[key])
    elif type(character[key]) is int:
        print(key, ":", character[key])
    elif type(character[key]) is dict:
        for key_list in character[key]:
            print(key_list, ":", character[key][key_list])
    elif type(character[key]) is list:
        count = 0
        for key_list in character[key]:
            print(key, ":", character[key][count])
            count = count + 1
