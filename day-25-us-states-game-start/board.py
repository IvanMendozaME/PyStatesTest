from turtle import Turtle, Screen

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.correctStates = 0
    def get_mouse_click_coor(self,x,y):
        print(x,y)
    def clickScreen(self):
        self.screen.onscreenclick(self.get_mouse_click_coor)
    def TextBox(self,correct):
        if correct == True:
            self.correctStates+=1
        answer_state = self.screen.textinput(title=f"{self.correctStates}/50 States Correct", prompt="Think in a state from US")
        return answer_state
    def updateBoard(self,state,position):
        self.goto(position)
        self.write(state, align="center", font=("Courier",10,"normal"))