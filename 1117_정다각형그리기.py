#다각형 그리기

import turtle

t = turtle.Turtle()
t.shape("turtle")

nPoint = int(input("그림 다각형 입력(3-8): "))
length = int(input("한 변의 길이 입력: "))
angle = 360/nPoint

for x in range(0, nPoint, 1):
    t.left(angle)
    t.forward(length)
