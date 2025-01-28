from turtle import Turtle

# Drawing mesh 
class Grid(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor('white')
        self.shapesize( 50,100)
        self.pensize(30)
        self.penup()
        self.starting_position_of_each_row = [(-220,220),(-220,70),(-220,-80)]
        self.pendown()
        self.draw_grid()

    def draw_square(self): # a function to draw a square that a the basic unit of the mesh
        for _ in range(4):
          self.forward(150)  # Move forward by 100 units
          self.right(90)     # Turn right by 90 degrees
    
    def draw_grid(self):
        for i in range(3):
            self.penup()
            self.goto(self.starting_position_of_each_row[i])
            for _ in range(3):
                self.pendown()
                self.draw_square()
                self.penup()
                self.forward(150)
                self.penup()

    