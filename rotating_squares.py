import turtle
my_turtle = turtle.Turtle()


#my_turtle.forward(100)
#my_turtle.circle(50)

def square(lenght,angle):
     for i in range(4):
        my_turtle.forward(lenght)
        my_turtle.right(angle)

for i in range(36):
    square(100,90)
    my_turtle.right(10)

total = 0
for i in range(10):
       my_turtle.right(90)
       my_turtle.forward(10)
       my_turtle.left(90)
       my_turtle.circle( total + 10)
