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

def UpdateString(string1,string2,index):
    S1LIST = string1.split(string1[3])
    separator = string2
    up_string = separator.join(S1LIST)
    return up_string

def FindWordCount(list1,a):
    space = ""
    string1 = space.join(list1)
    i = 0
    count = 0
    for s in string1:
        if a in string1[5:]:
            count += 1
            i += string1.find(a)
            #print(i)
    print(count)

