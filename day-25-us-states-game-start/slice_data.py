import pandas

class Data():
    def __init__(self) -> None:
        data = pandas.read_csv("50_states.csv")
        self.df = pandas.DataFrame(data)
    def ListStates(self):
        States = self.df["state"].to_list()
        States = [state.lower() for state in States]
        return States
    def GetCoordinates(self):
        x_list = self.df["x"].to_list()
        y_list = self.df["y"].to_list()
        coordinates = []
        for i in range(len(x_list)):
            coordinates.append((x_list[i],y_list[i]))
        return coordinates