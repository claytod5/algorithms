"""a recursive program to display a Koch snowflake."""

import turtle


def draw_triangle(points, my_turtle):
    """Draw triangle

    :param points: Nested list of coordinate pairs
    :param my_turtle: Turtle object

    """
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])


def koch_snowflake(points, depth, my_turtle):
    """Recursively draw Koch Snowflake of certain depth

    :param points: nested list of coordinate pairs
    :param depth: number of iterations
    :param my_turtle: Turtle object

    """
