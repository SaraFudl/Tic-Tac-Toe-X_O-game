from turtle import Turtle, Screen
import time

screen = Screen()

class Symbols(Turtle): # a class to draw x and o
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.pencolor('white')
        self.shapesize(5, 5)
        self.pensize(15)
        self.clicked_positions_inside_squares = []
        

    def get_square_center(self, x, y):
        # Map the click coordinates to the nearest grid square center
        grid_size = 150
        x_center = round(x / grid_size) * grid_size
        y_center = round(y / grid_size) * grid_size
        return x_center, y_center

    def draw_X_at_click(self,x, y):
        self.penup()
        self.goto(x, y)
        self.pendown()
        self.setheading(45)
        for _ in range(4):
            self.forward(50)
            self.backward(50)
            self.right(90)

    def draw_O_at_click(self, x, y):
        self.penup()
        self.goto(x, y - 25)
        self.pendown()
        self.circle(25)

    def avoid_double_click_in_one_square(self,clicked_positions_inside_squares,pos):
        for position in clicked_positions_inside_squares:
            if pos == position: # to check if the clicked position already found in previously clicked positions 
                print("not allowed double click")
