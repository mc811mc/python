import turtle;

turtle.title("My Wonderful Tree")

pen = turtle.Turtle();
pen.shape("turtle");
pen.speed(100);
pen.setheading(90);

def draw_branch():
    pen.color("brown")
    pen.forward(40)

draw_branch()

def draw_branch(len):
    pen.color("brown")
    pen.forward(len)

draw_branch(40)

def draw_branch(len):
    pen.color("brown")
    pen.forward(len)
    pen.right(25)
    draw_branch(len)

def draw_branch(len):
    pen.color("brown")
    pen.forward(len)
    pen.right(25)
    draw_branch(len - 5)

def draw_branch(len):
    if (len > 5):
        pen.color("brown")
        pen.forward(len)
        pen.right(25)
        draw_branch(len - 5)

def draw_branch(len):
    if (len > 5):
        pen.color("brown")
        pen.forward(len)
        pen.right(25)
        draw_branch(len - 5)
        pen.left(50)
        draw_branch(len -5)
        pen.right(25)
        pen.backward(len)

draw_branch(40)

turtle.Screen().exitonclick()