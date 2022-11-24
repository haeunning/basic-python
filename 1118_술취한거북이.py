#술 취한 거북이
#for문을 이용하여 거북이가 술에 취한 것처럼 랜덤하게 움직이도록 프로그램을 작성해보자.
#--->난수를 이용하기

import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for i in range(30):
    length = random.randint(1,100)
    angle = random.randint(-180,200)
    t.forward(length)
    t.right(angle)
