from enum import Enum
import sys

class Cha(Enum):
    DIT = 1
    DAT = 2
    LETTERSPACE = 3
    SPACE = 4

class DotDashtoText():
    outputText = ""

    morseTable = {
        ".-":     "A",
        "-...":   "B",
        "-.-.":   "C",
        "-..":    "D",
        ".":      "E",
        "..-.":   "F",
        "--.":    "G",
        "....":   "H",
        "..":     "I",
        ".---":   "J",
        "-.-":    "K",
        ".-..":   "L",
        "--":     "M",
        "-.":     "N",
        "---":    "O",
        ".--.":   "P",
        "--.-":   "Q",
        ".-.":    "R",
        "...":    "S",
        "-":      "T",
        "..-":    "U",
        "...-":   "V",
        ".--":    "W",
        "-..-":   "X",
        "-.--":   "Y",
        "--..":   "Z",
        ".--.-":  "Å",
        ".-.-":   "Ä",
        "---.":   "Ö",
        "-----":  "0",
        ".----":  "1",
        "..---":  "2",
        "...--":  "3",
        "....-":  "4",
        ".....":  "5",
        "-....":  "6",
        "--...":  "7",
        "---..":  "8",
        "----.":  "9",
        ".-.-.-": ".",
        "-.-.-.": ";",
        "--..--": ",",
        "---...": ":",
        "-.-.--": "!",
        "..--..": "?",
        "-...-":  "=",
    }

    def __init__(self) -> None:
        pass

    def recieveSequence(self, dotDashSequence: list):
        #print(dotDashSequence)

        endOfWord = False
        if dotDashSequence[-1] == Cha.SPACE:
            endOfWord = True
        dotDashSequence.pop()
        if len(dotDashSequence) < 1:
            self.outputText = self.outputText + " "
            return

        dotDashString = ""
        for cha in dotDashSequence:
            if cha == Cha.DIT:
                dotDashString = dotDashString + "."
            else:
                dotDashString = dotDashString + "-"

        self.outputText = self.outputText + self.morseTable.get(dotDashString, "")
        if endOfWord:
            self.outputText = self.outputText + " "

        print(f'\r{self.outputText}', end='', flush=True)

    def reset_string(self):
        self.outputText = ""
        #sys.stdout.write("\033[K")
        sys.stdout.write('\033[2K\033[1G')
        sys.stdout.flush()
        #print('\r' + ' '*100, end='', flush=True)







