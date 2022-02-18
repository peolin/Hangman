gallows = [
    ["____________________", '   |', '   |', '   |', '   |', '   |', '----------  '],
    ["____________________","   |               |", '   |', '   |', '   |', '   |', '----------  '],
    ["____________________","   |               |","   |               O", '   |', '   |', '   |', '----------  '],
    ["____________________","   |               |","   |               O", "   |               |", '   |', '   |', '----------  '],
    ["____________________","   |               |","   |               O", "   |             / |", '   |', '   |', '----------  '],
    ["____________________","   |               |","   |               O", "   |             / | \\", '   |', '   |', '----------  '],
    ["____________________","   |               |","   |               O", "   |             / | \\", "   |              /", '   |', '----------  '],
    ["____________________","   |               |","   |               O", "   |             / | \\", "   |              / \\", "   |", "----------  "]]

def gallows_type(lives):
    if lives == 7:
        for sym in gallows[0]:
            print(str(sym))
    elif lives == 6:
        for sym in gallows[1]:
            print(str(sym))       
    elif lives == 5:
        for sym in gallows[2]:
            print(str(sym)) 
    elif lives == 4:
        for sym in gallows[3]:
            print(str(sym)) 
    elif lives == 3:
        for sym in gallows[4]:
            print(str(sym)) 
    elif lives == 2:
        for sym in gallows[5]:
            print(str(sym)) 
    elif lives == 1:
        for sym in gallows[6]:
            print(str(sym)) 
    elif lives == 0:
        for sym in gallows[7]:
            print(str(sym)) 