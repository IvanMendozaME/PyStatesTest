import turtle 
from slice_data import Data
from board import Board
screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = Data()
Coordinates = data.GetCoordinates()
States = data.ListStates()

bd = Board() 
bd.clickScreen()
answer = bd.TextBox(False).lower()
corrects = []
while len(corrects)<50:
    
    if answer in States:
        position = Coordinates[States.index(answer)]
        bd.updateBoard(answer,position)
        answer = bd.TextBox(True).lower()
        corrects.append(answer)
        
turtle.mainloop()