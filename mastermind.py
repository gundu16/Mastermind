c = 0
c1 = 0
l1 = []
l2 = []
sc = 0
print("WELCOME TO MASTERMIND GAME !!!!")
print("...............")
print("ABOUT THE GAME")
print("1. Its a two player game")
print("2. First player gives any four numbers from(1 to 6) for which each number will be having corresponding colour ") 
print("3. Note there should not be any two same numbers")
print("3. Second player should guess that four colours from  the list[blue,green,yellow,pink,black,orange]")
print("4. And also the position of the colours should be same as of the first player's")
print("5. The player will have 12 chances")
print("6. The maximum score the player gets is 100")
print("4. If the colour given by the second player is present in the list given by the first player and is in correct position RED will be displayed")
print("5. If the colour is present in the list but not in the correct position WHITE colour will be displayed")
print("........................")
print("RULES FOR THE GAME")
print("1. Player should enter only four colours")
print("2. And the four colours should be different")
print(".......................")
print("First player input(enter first number and press enter and then input second number so on.. upto four numbers)")
for i in range(0,4):
    # first player input
    x1 = int(input())
    if(x1 == 1):
        x11 = "blue"
        l1.append(x11)
    elif(x1 == 2):
        x11 = "green"
        l1.append(x11)
    elif(x1 == 3):
        x11 = "yellow"
        l1.append(x11)
    elif(x1 == 4):
        x11 = "pink"
        l1.append(x11)
    elif(x1 == 5):
        x11 = "black"
        l1.append(x11)
    else:
        x11 = "orange"
        l1.append(x11)
for i in range(1, 13):
    # second player input
    print("second player input(enter first colour and press enter and then the input second colour so on.. upto four colurs)")
    l2 = []
    l3 = []
    l4 = []
    sc += 1
    for i in range(0,4):
        x2 = input()
        x3 = x2.lower()
        l2.append(x3)
    c = 0
    for i in range(0,4):
        if(l1[i] == l2[i]):
            c += 1
    if(c == 4):
        print("win")
        print("congratulations")
        if(sc == 1):
            print("score is 100")
            print("great job !!")
            print("you have completed in one attempt")
        elif(sc == 2):
            print("score is 90")
            print("you have completed in two attempts")
        elif(sc == 3):
            print("score is 80")
            print("you have completed in three attempts")
        elif(sc == 4):
            print("score is 70")
            print("you have completed in four attempts")
        elif(sc == 5):
            print("score is 60")
            print("you have completed in five attempts")
        elif(sc == 6):
            print("score is 50")
            print("you have completed in six attempts")
        elif(sc == 7):
            print("score is 40")
            print("you have completed in seven attempts")
        elif(sc == 8):
            print("score is 30")
            print("you have completed in eight attempts")
        elif(sc == 9):
            print("score is 20")
            print("you have completed in nine attempts")
        elif(sc == 10):
            print("score is 15")
            print("you have completed in ten attempts")
        elif(sc == 11):
            print("score is 10")
            print("you have completed in eleven attempts")
        else:
            print("score is 5")
            print("you have completed in twelve attempts")
        break
    else:
        for i in range(0,4):
            for j in range(0,4):
                if(l1[i] == l2[j]):
                    if(i == j):
                     #when colour is present at the correct position
                        l3.append("red")
                    else:
                    #when colour is present but in the wrong position
                        l3.append("white")
        print(l3)
    c1 += 1
    if(c1 == 12):
        print("out") #when 12 chances are completed
        print("sorry you were left with no chances")
        print("score is 0")


