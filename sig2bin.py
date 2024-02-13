import time
#import OnOfftoDotDash
from typing import Any


threshold = 90 # Placeholder angle for activation

class databank:
    state = False
    time = 0
    def setState(self, newState):
        self.state = newState
    def setTime(self):
        self.time = time()


def sigToBin(deg, databank):
    if deg > threshold: # active state read
        if not databank.state: # going into active
            timediff = (time() - databank.time)*1000 # time we spent in passive state (in ms)
            databank.setState(databank, True) # set state to active
            databank.setTime(databank) # refresh timestamp
            # recieveState(False, timediff)
        # already in active, do nothing
            
    else: # passive state read
        if databank.state: # going into passive
            timediff = (time() - databank.time)*1000 # time we spent in active state (in ms)
            databank.setState(databank, False) # set state to passive
            databank.setTime(databank) # refresh timestamp
            #recieveState(True, timediff)
        # already in passive, do nothing

