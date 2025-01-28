from turtle import Screen
from drawing_grid import Grid
from symbols_X_O import Symbols 
from scoreboard import Scoreboard
import time

# setting up the screen
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Tic Tac Toe")
screen.tracer(0)

# creating objects
grid = Grid()
symbols = Symbols()
X_score_ob = Scoreboard((-300,300))
X_score_ob.update_score_X()

O_score_ob = Scoreboard((300,300))
O_score_ob.update_score_O()

final_score = Scoreboard((0,-350))
screen.update()


def is_click_in_square(pos):
    x, y = pos
    # Upper row
    if (-225 <= x <= -75) and (75 <= y <= 225):
        return True
    if (-75 <= x <= 75) and (75 <= y <= 225):
        return True
    if (75 <= x <= 225) and (75 <= y <= 225):
        return True
    # Middle row
    if (-225 <= x <= -75) and (-75 <= y <= 75):
        return True
    if (-75 <= x <= 75) and (-75 <= y <= 75):
        return True
    if (75 <= x <= 225) and (-75 <= y <= 75):
        return True
    # Lower row
    if (-225 <= x <= -75) and (-225 <= y <= -75):
        return True
    if (-75 <= x <= 75) and (-225 <= y <= -75):
        return True
    if (75 <= x <= 225) and (-225 <= y <= -75):
        return True
    return False


def handle_click( x, y):
    global is_x_turn
    x_center, y_center = symbols.get_square_center(x, y) # Getting the x and y cors of symbols
    symbols.penup() 
    screen.onclick(symbols.goto(x_center, y_center),btn=1)#check the pos of the clicked point before drawing x or o to check if the clicked point is inside or outside the squares
    x_center, y_center = symbols.get_square_center(x, y)
    pos = symbols.pos()

    if is_click_in_square(pos):
        if pos in symbols.clicked_positions_inside_squares:# to check if the clicked position already found in previously clicked positions 
             pass
        else:
            if is_x_turn:
                symbols.draw_X_at_click(x_center, y_center)
                symbols.clicked_positions_inside_squares.append(pos)
                X_score_ob.list_of_X.append((x_center, y_center))
                X_score_ob.cases_of_win_X()
            else:
                symbols.draw_O_at_click(x_center, y_center)
                symbols.clicked_positions_inside_squares.append(pos)
                O_score_ob.list_of_O.append((x_center, y_center))
                O_score_ob.cases_of_win_O()
            is_x_turn = not is_x_turn  # Switch turns
    else:
          print("not allowed")


is_x_turn = True
game_on = True
while game_on:
     screen.tracer(1)
     screen.onclick(handle_click,btn=1)
     screen.update()
     # check if all the squares of the mesh are occupied or not to finish the game
     if len(symbols.clicked_positions_inside_squares) == 9:
        print("game_over")
        game_on = False 
        #check who is the winner X player or O player by checking the final score of each
        if X_score_ob.X_score > O_score_ob.O_score:
            final_score.write(f"The winner is X_player \n The final score of X_player is {X_score_ob.X_score} \n The final score of O_player is {O_score_ob.O_score}",align="center", font=("Arial", 15, "normal"))
        elif O_score_ob.O_score > X_score_ob.X_score: 
            final_score.write(f"The winner is O_player \n The final score of X_player is {X_score_ob.X_score} \n The final score of O_player is {O_score_ob.O_score}",align="center", font=("Arial", 15, "normal"))
        else:
            final_score.write(f"It's a tie \n The final score of X_player is {X_score_ob.X_score} \n The final score of O_player is {O_score_ob.O_score}",align="center", font=("Arial", 15, "normal"))
 
screen.mainloop()