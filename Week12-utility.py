#Method Used
#Dylan Broderick
#CSCI102 - Section E
#Week 12 - Part A

def PrintOutput(s):
    print("OUTPUT",s)

def LoadFile(file):
    text = open(file)
    lines = []
    for line in text:
        lines.append(line)
    return lines

