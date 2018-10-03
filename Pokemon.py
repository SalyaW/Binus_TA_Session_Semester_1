print("Hello world") #for goodluck and also a safety net
import random
data = []
playerx = 0
playery = 0
before = 0
def read():#Reads the .txt file
    global before
    file = open("pkmn_map.txt", "r")
    for row in file:
        if (len(row)>3):
            temp = []
            raw = row.split(" ")
            for i in range(0,8):
                if i == 7:
                    temp.append(str(int(raw[i])))
                elif i in range(0,7):
                    temp.append(raw[i])
            data.append(temp)
        else:
            before = row
    file.close()

def view(): #Translates the .txt file into map
    global playerx,playery
    for i in range (0,8):
        for j in range (0,8):
            if data[i][j] == "2":
                print("#",end=" ")
            elif data[i][j] == "1":
                playerx = i
                playery = j
                print("X",end=" ")
            elif data[i][j] == "0":
                print(data[i][j],end=" ")
        print("")
    print (playerx,playery)
read()
def write():
    temp = ""
    file = open("pkmn_map.txt","w")
    for i in range(0,8):
        for p in range (0,8):
            temp = temp + data[i][p]
            if (p !=7):
                temp = temp+' '
            else:
                temp = temp + "\n"
    temp = temp + before
    file.write(temp)
    file.close()

def encounter():
    a=random.randint(0,3)
    if not a:
        print("You found something!")


while 1:#Loops the menu
    view()
    print("Pokémon Bootleg Ver.")
    print("===================")
    print("        MENU       ")
    print("===================")
    print("1.Move up")
    print("2.Move down")
    print("3.Move left")
    print("4.Move right")
    print("5.Save and Exit")
    c = input("Choose an option:")
    print("")
    if c=="1":
        if playerx - 1 >= 0:
            data[playerx][playery] = before
            playerx -= 1
            if (data[playerx][playery]== "2"):
                encounter()
            before = data[playerx][playery]
            data[playerx][playery]="1"
    elif c=="2":
        if playerx + 1 >= 0:
            data[playerx][playery] = before
            playerx += 1
            if (data[playerx][playery]== "2"):
                encounter()
            before = data[playerx][playery]
            data[playerx][playery]="1"
    elif c=="3":
        if playery - 1 >= 0:
            data[playerx][playery] = before
            playery -= 1
            if (data[playerx][playery]== "2"):
                encounter()
            before = data[playerx][playery]
            data[playerx][playery]="1"
    elif c=="4":
        if playery + 1 >= 0:
            data[playerx][playery] = before
            playery += 1
            if (data[playerx][playery]== "2"):
                encounter()
            before = data[playerx][playery]
            data[playerx][playery]="1"
    elif c=="5":
        write()
        print("Exited")
        break
    else:
        print("Wrong input you fool!")
    print("")

