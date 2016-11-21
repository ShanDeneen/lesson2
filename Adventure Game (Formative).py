vName=input("Please enter your name: ")
print("Hello",vName)
def tentacle():
    print("You have been trapped inside a giant octopus's stomach.You can try and exit through any of the octopus's 8 tentacles.")
    choice= input("Choose a number between 1 & 8: ")
    if choice != "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8":
        if choice== "1":
            print("Sorry there was an ink malfunction, you died")
        elif choice== "5":
            print("You have entered a dark sea tunnel.")
            print(seatunnel())
        elif choice== "2":
            print("Sorry there was an ink malfunction, you died")
        elif choice== "6":
            print("You have entered a dark sea tunnel.")
            print(seatunnel())
        elif choice== "3":
            print("Sorry there was an ink malfunction, you died")
        elif choice== "7":
            print("You have entered a dark sea tunnel.")
            print(seatunnel())
        elif choice== "4":
            print("Sorry there was an ink malfunction, you died")
        elif choice== "8":
            print("You have entered a dark sea tunnel.")
            print(seatunnel())
        else:
            print("Sorry, that tentacle does not exist.")
def seatunnel():
    print("You have arrived in a dark sea tunnel. There are two paths before you. You can either go right or left.")
    direction= input("Choose right or left: ")
    if direction !="right"or"left":
        if direction=="right":
            print("Sorry, you have run into a dead end and there is no air left. You died.")
        elif direction=="left":
            print("You find a mysterious satchel.")
            print(satchel())
        else:
            print("Sorry, that was not an option. Try again.")
def satchel():
    print("You have picked up the mysterious satchel. Inside you find a scuba mask and a potato gun.")
    choice2= input("Do you want to pick up the scuba mask or the potato gun?: ")
    if choice2 !="scuba mask" or "potato gun":
        if choice2=="scuba mask":
            print("You grab the scuba mask and put it on.")
            print(scubamask())
        elif choice2=="potato gun":
            print("You take the potato gun and the potato bullets.")
            print(potate())
        else:
            print("Sorry, that was not an option. Try again.")
def potate():
    print("You are hungry. You have potatoes. You can choose to eat or keep the potatoes.")
    hunger= input("Eat or keep?: ")
    if hunger != "eat"or"keep":
        if hunger== "eat":
            print("Sorry, you are allergic to potatoes. You died.")
        elif hunger== "keep":
            print("You keep the potato gun and keep walking through the sea tunnel. Eventually you encounter a giant seahorse. You try and defend yourself, but cannot beat the seahorse. You die of exhaustion.")
        else:
            print("Sorry,that is not an option. Please try again.")
def scubamask():
    print("After you put your mask on you approach a hole in the sea tunnel. You can use your mask and swim through it or stay and explore.")
    swim=input("Swim or explore?: ")
    if swim != "swim" or "explore":
        if swim== "explore":
            print("You decided to stay and eplore the tunnel. After 5 minutes your oxygen tank explodes and you died.")
        elif swim== "swim":
            print("After you exit the tunnel through the hole, you see the shore and swim to it. Congrats! You survived. ")
        else:
            print("Sorry,that is not an option. Please try again.")
print(tentacle())
