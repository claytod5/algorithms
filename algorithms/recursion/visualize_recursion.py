import turtle


def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)


def tree(branch_len, t):
    t.pensize(branch_len // 15)

    if branch_len <= 15:
        t.color("green")
    else:
        t.color("brown")

    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)

        if branch_len > 15:
            t.color("brown")
        t.backward(branch_len)


if __name__ == "__main__":
    # my_turtle = turtle.Turtle()
    # my_win = turtle.Screen()
    # draw_spiral(my_turtle, 100)
    # my_win.exitonclick()
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75, t)
    my_win.exitonclick()
