#거북이 제어하기
#L을 입력하면 거북이가 왼쪽으로 100 이동, R을 입력하면 거북이가 오른쪽으로 100이동

import turtle
t = turtle.Turtle()
t.shape("turtle")

while True:
    command = input("명령 입력: ")
    if command =='l':
        t.left(90)
        t.forward(100)
    elif command == 'r':
        t.right(90)
        t.forward(100)
    elif command =='q':
        break
