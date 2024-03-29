from time import time
from OnOfftoDotDash import *
from typing import Any



class Databank:
    state = False
    spacedL = True
    spacedW = True
    time = 0
    dotDash = OnOfftoDotDash(14)

    def __init__(self, threshold = 30):
        self.threshold = threshold

    def setState(self, newState):
        self.state = newState

    def setTime(self):
        self.time = time()

    def sigToBin(self, deg):
        #print(f"\r{deg}", end="")
        if abs(deg) > self.threshold: # active state read
            if not self.state: # going into active
                self.setState(True) # set state to active
                self.setTime() # refresh timestam
            # already in active, do nothing
            
        else: # passive state read
            if self.state: # going into passive
                timediff = (time() - self.time)*1000 # time we spent in active state (in ms)
                self.setState(False) # set state to passive
                self.setTime() # refresh timestamp
                self.spacedL, self.spacedW = False, False
                self.dotDash.recieveState(True, timediff)
            # checking if we should add a space
            else:
                timediff = (time() - self.time)*1000 # time we spent in passive state
                if timediff > self.dotDash.wpmToms() * 2.5 and not self.spacedL:
                    self.spacedL = True
                    self.dotDash.recieveState(False, timediff)
                if timediff > self.dotDash.wpmToms() * 6.5 and not self.spacedW:
                    self.spacedW = True
                    self.dotDash.recieveState(False, timediff)

    def reset_string(self):
        self.dotDash.reset_string()

