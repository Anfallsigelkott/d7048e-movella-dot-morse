from DotDashtoText import DotDashtoText, Cha

class OnOfftoDotDash():
    dotDashtoText = DotDashtoText()
    wpm = 14
    outputDotDashSequence = []

    def __init__(self, wpm) -> None:
        self.wpm = wpm

    def recieveState(self, state, time):
        if state:
            if time < self.wpmToms() * 2.5: # TODO: Adjust forgiving timing
                self.outputDotDashSequence.append(Cha.DIT)
            else:
                self.outputDotDashSequence.append(Cha.DAT)
        else:
            if time < self.wpmToms() * 2.5:
                pass # Dot-dash space
            elif time < self.wpmToms() * 6.5:
                self.outputDotDashSequence.append(Cha.LETTERSPACE)
                self.dotDashtoText.recieveSequence(self.outputDotDashSequence)
                self.outputDotDashSequence.clear()
            else:
                self.outputDotDashSequence.append(Cha.SPACE)
                self.dotDashtoText.recieveSequence(self.outputDotDashSequence)
                self.outputDotDashSequence.clear()

    def wpmToms(self):
        return (1200 / self.wpm)
    
    def reset_string(self):
        self.dotDashtoText.reset_string()


if __name__ == '__main__':
    onOff = OnOfftoDotDash(14)    

    onOff.recieveState(True, 300)
    onOff.recieveState(False, 300)

    onOff.recieveState(True, 100)
    onOff.recieveState(False, 100)
    onOff.recieveState(True, 100)
    onOff.recieveState(False, 100)
    onOff.recieveState(True, 100)
    onOff.recieveState(False, 100)
    onOff.recieveState(True, 100)
    onOff.recieveState(False, 300)

    onOff.recieveState(True, 100)
    onOff.recieveState(False, 600)



    onOff.recieveState(True, 100)
    onOff.recieveState(False, 100)
    onOff.recieveState(True, 300)
    onOff.recieveState(False, 600)

    onOff.recieveState(True, 300)
    onOff.recieveState(False, 100)
    onOff.recieveState(True, 100)
    onOff.recieveState(False, 100)
    onOff.recieveState(True, 100)
    onOff.recieveState(False, 100)
    onOff.recieveState(True, 100)
    onOff.recieveState(False, 600)

    onOff.recieveState(True, 300)
    onOff.recieveState(False, 100)
    onOff.recieveState(True, 100)
    onOff.recieveState(False, 100)
    onOff.recieveState(True, 300)
    onOff.recieveState(False, 100)
    onOff.recieveState(True, 100)
    onOff.recieveState(False, 600)