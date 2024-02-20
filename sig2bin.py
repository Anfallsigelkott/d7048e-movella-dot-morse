import time
import OnOfftoDotDash
from typing import Any



class databank:
    state = False
    time = 0
    dotDash = OnOfftoDotDash()
    threshold = 90 # Placeholder angle for activation


    def setState(self, newState):
        self.state = newState

    def setTime(self):
        self.time = time()

    def sigToBin(self, deg):
        if deg > self.threshold: # active state read
            if not self.state: # going into active
                timediff = (time() - self.time)*1000 # time we spent in passive state (in ms)
                self.setState(self, True) # set state to active
                self.setTime(self) # refresh timestamp
                self.dotDash.recieveState(self, False, timediff)
            # already in active, do nothing
            
        else: # passive state read
            if self.state: # going into passive
                timediff = (time() - self.time)*1000 # time we spent in active state (in ms)
                self.setState(self, False) # set state to passive
                self.setTime(self) # refresh timestamp
                self.dotDash.recieveState(self, True, timediff)
            # already in passive, do nothing

