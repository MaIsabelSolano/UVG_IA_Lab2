import pandas as pd
from decimal import *

class RB:
    def __init__(self, input):
        self.data = {}

        self.genRB(input)

        print(self.data)


    def genRB(self, input):
        
        df = pd.read_csv(input, sep = "=", header = None)

        for i in range(len(df[0])):
            self.data[
                self.getEvent(df[0].__getitem__(i))
            ] = df[1].__getitem__(i)

    def getEvent(self, E):
        E_temp = str(E)
        E_temp = E_temp.replace("P(", "")
        E_temp = E_temp.replace(") ", "")

        return E_temp

    def readEvent(self): 
        0

    def P(self, Event):
        # Find if self.data has already the query
        try:
            return self.data[Event]

        except:
            print('No existe')