import turtle


arrow=turtle.Turtle()
arrow.getscreen().bgcolor("#994444")
def star(arrow):

    arrow.color("red","black")
    arrow.speed(8)
    arrow.begin_fill()

    for i in range (12):
        arrow.forward(200)
        arrow.left(150)
    arrow.end_fill()

number_stars1 = input("Enter number of stars you want me to draw:")
number_stars = int (number_stars1)

for i in range (number_stars):
    star(arrow)
    arrow.penup()
    arrow.forward(200)
    arrow.pendown()

turtle.done()