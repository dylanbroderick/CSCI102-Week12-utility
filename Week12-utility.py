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

def ScoreFinder(players,scores,NAME):
    i = 0
    for player in players:
        players[i] = players[i].lower()
        i += 1
    name = NAME.lower()
    n = 0
    name_in_list = False
    for player in players:
        if name == player:
            name_in_list = True
            N = n
            break
        n += 1
    if name_in_list == True:
        print("OUTPUT",NAME,"got a score of",scores[N])
    else:
        print("OUTPUT player not found")

def Union(list1,list2):
    dup_list = list1 + list2
    out_list = []
    for i in dup_list:
        if i not in out_list:
            out_list.append(i)
    return out_list

def Intersection(list1,list2):
    intersection = []
    for i in list2:
        if i in list1:
            intersection.append(i)
    return intersection

def NotIn(list1,list2):
    notinlist2 = []
    for i in list1:
        if i not in list2:
            notinlist2.append(i)
    return notinlist2
