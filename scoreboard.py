from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.X_score = 0
        self.O_score =0
        self.pencolor("red")
        self.list_of_X = []
        self.list_of_O = []
        # to win horizontally
        self.upper_row = [(-150, 150), (0, 150), (150, 150)]
        self.middle_row = [(-150, 0), (0, 0), (150, 0)]
        self.lower_row = [(-150, -150), (0, -150), (150, -150)]
        # to win vertically
        self.left_column = [(-150, 150), (-150, 0), (-150, -150)]
        self.middle_column = [(0, 150), (0, 0), (0, -150)]
        self.right_column = [(150, 150), (150, 0), (150, -150)]
        # to win diagonally
        self.tuples_to_win_diagnolR = [(-150, 150), (0, 0), (150, -150)]
        self.tuples_to_win_diagnolL = [(150, 150), (0, 0), (-150, -150)]
        self.applied_wins = []  # a list of identifiers for each win condition to avoid multiple wins

    def cases_of_win_X(self):
        if 3 <= len(self.list_of_X) <= 9:
            # horizontal win the same Y coordinates
            filtered_upper = [t for t in self.list_of_X if t in self.upper_row]
            filtered_middle_row = [t for t in self.list_of_X if t in self.middle_row]
            filtered_lower = [t for t in self.list_of_X if t in self.lower_row]
            if "upper_row_winx" not in self.applied_wins and sorted(filtered_upper) == sorted(self.upper_row):
                self.increase_score_X()
                print("upper_row_winx")
                self.applied_wins.append("upper_row_winx")
            if "middle_row_winx" not in self.applied_wins and sorted(filtered_middle_row) == sorted(self.middle_row):
                self.increase_score_X()
                print("middle_row_winx")
                self.applied_wins.append("middle_row_winx")
            if "lower_row_winx" not in self.applied_wins and sorted(filtered_lower) == sorted(self.lower_row):
                self.increase_score_X()
                print("lower_row_winx")
                self.applied_wins.append("lower_row_winx")

            # vertical win the same X coordinates
            filtered_right = [t for t in self.list_of_X if t in self.right_column]
            filtered_middle_column = [t for t in self.list_of_X if t in self.middle_column]
            filtered_left = [t for t in self.list_of_X if t in self.left_column]
            if "right_column_winx" not in self.applied_wins and sorted(filtered_right) == sorted(self.right_column):
                self.increase_score_X()
                print("right_column_winx")
                self.applied_wins.append("right_column_winx")
            if "middle_column_winx" not in self.applied_wins and sorted(filtered_middle_column) == sorted(self.middle_column):
                self.increase_score_X()
                print("middle_column_winx")
                self.applied_wins.append("middle_column_winx")
            if "left_column_winx" not in self.applied_wins and sorted(filtered_left) == sorted(self.left_column):
                self.increase_score_X()
                print("left_column_winx")
                self.applied_wins.append("left_column_winx")

            # diagonal win
            filtered_diagnolR = [t for t in self.list_of_X if t in self.tuples_to_win_diagnolR]
            filtered_diagnolL = [t for t in self.list_of_X if t in self.tuples_to_win_diagnolL]
            if "tuples_to_win_diagnolR_winx" not in self.applied_wins and sorted(filtered_diagnolR) == sorted(self.tuples_to_win_diagnolR):
                self.increase_score_X()
                print("tuples_to_win_diagnolR_winx")
                self.applied_wins.append("tuples_to_win_diagnolR_winx")
            if "tuples_to_win_diagnolL_winx" not in self.applied_wins and sorted(filtered_diagnolL) == sorted(self.tuples_to_win_diagnolL):
                self.increase_score_X()
                print("tuples_to_win_diagnolL_winx")
                self.applied_wins.append("tuples_to_win_diagnolL_winx")

    def cases_of_win_O(self):
        if 3 <= len(self.list_of_O) <= 9:
            # horizontal win the same Y coordinates
            filtered_upper = [t for t in self.list_of_O if t in self.upper_row]
            filtered_middle_row = [t for t in self.list_of_O if t in self.middle_row]
            filtered_lower = [t for t in self.list_of_O if t in self.lower_row]
            if "upper_row_wino" not in self.applied_wins and sorted(filtered_upper) == sorted(self.upper_row):
                self.increase_score_O()
                print("upper_row_wino")
                self.applied_wins.append("upper_row_wino")
            if "middle_row_wino" not in self.applied_wins and sorted(filtered_middle_row) == sorted(self.middle_row):
                self.increase_score_O()
                print("middle_row_wino")
                self.applied_wins.append("middle_row_wino")
            if "lower_row_wino" not in self.applied_wins and sorted(filtered_lower) == sorted(self.lower_row):
                self.increase_score_O()
                print("lower_row_wino")
                self.applied_wins.append("lower_row_wino")

            # vertical win the same X coordinates
            filtered_right = [t for t in self.list_of_O if t in self.right_column]
            filtered_middle_column = [t for t in self.list_of_O if t in self.middle_column]
            filtered_left = [t for t in self.list_of_O if t in self.left_column]
            if "right_column_wino" not in self.applied_wins and sorted(filtered_right) == sorted(self.right_column):
                self.increase_score_O()
                print("right_column_wino")
                self.applied_wins.append("right_column_wino")
            if "middle_column_wino" not in self.applied_wins and sorted(filtered_middle_column) == sorted(self.middle_column):
                self.increase_score_O()
                print("middle_column_wino")
                self.applied_wins.append("middle_column_wino")
            if "left_column_wino" not in self.applied_wins and sorted(filtered_left) == sorted(self.left_column):
                self.increase_score_O()
                print("left_column_wino")
                self.applied_wins.append("left_column_wino")

            # diagonal win
            filtered_diagnolR = [t for t in self.list_of_O if t in self.tuples_to_win_diagnolR]
            filtered_diagnolL = [t for t in self.list_of_O if t in self.tuples_to_win_diagnolL]
            if "tuples_to_win_diagnolR_wino" not in self.applied_wins and sorted(filtered_diagnolR) == sorted(self.tuples_to_win_diagnolR):
                self.increase_score_O()
                print("tuples_to_win_diagnolR_wino")
                self.applied_wins.append("tuples_to_win_diagnolR_wino")
            if "tuples_to_win_diagnolL_wino" not in self.applied_wins and sorted(filtered_diagnolL) == sorted(self.tuples_to_win_diagnolL):
                self.increase_score_O()
                print("tuples_to_win_diagnolL_wino")
                self.applied_wins.append("tuples_to_win_diagnolL_wino")

    def update_score_X(self):
        self.clear()
        self.write(f"X_Score =  {self.X_score}", align="center", font=("Arial", 28, "normal"))

    def increase_score_X(self):
        self.clear()
        self.X_score += 1
        self.update_score_X()

    def update_score_O(self):
        self.clear()
        self.write(f"O_Score = {self.O_score}", align="center", font=("Arial", 28, "normal"))

    def increase_score_O(self):
        self.clear()
        self.O_score += 1
        self.update_score_O()
    
