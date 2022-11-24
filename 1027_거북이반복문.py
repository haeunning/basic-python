import turtle

myT=None

myT=turtle.Turtle()
myT.shape('Turtle')

for j in range(0,4):
    for i in range(0,4):
        myT.forward(200)
        myT.right(90)
    myT.forward(-30)
    
turtle.done()

