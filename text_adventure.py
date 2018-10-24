import random
import time


#create the rooms
room=[]
for i in range(10):
    if i==0:
        a={}
    else:
        a={'apple':random.randint(0,3),'box':random.randint(0,2),'bullet':random.randint(0,5),'map':random.randint(0,1),'knife':random.randint(0,1)}
    room.append(dict(a))
rightroom=random.randint(1,10)
print(rightroom)
room[rightroom].update({'THE GOLEDN DONUTS':1})
print(room[rightroom])
#some code to make sure the rooms are created right
def nouse():

    for i in range(10):
        print('room',i,'apple',room[i].get('apple'),'boxes',room[i].get('box'))
    print(room[5])
    room[5]['apple']=6
    print(room[5])
#nouse()

#basic commands
def go_up():
    if currentRoom>=9:
        time.sleep(1)
        print("You can't go higher! ")
    else:
        currentRoom +=2
def go_down():
    if currentRoom<=1:
        time.sleep(1)
        print("You can't go lower! ")
    else:
        currentRoom -=2
def go_left():
    if currentRoom%2==0:
        time.sleep(1)
        print("There is no door on that wall ")
    else:
        currentRoom -=1
def go_right():
    if currentRoom%2==1:
        time.sleep(1)
        print("There is no door on that wall ")
    else:
        currentRoom +=1

def lookroom():
    i=currentRoom
    time.sleep(1)
    print("With your sharp eyes you are seeing: ")
    keys=list(room[i].keys())
    values=list(room[i].values())
    for j in range(len(room[5])):
        print(keys[j]," ",values[j])


def look_item(key):
    j=list(playerInv.keys())
    i=currentRoom
    keys=list(room[i].keys())
    if key not in keys or j :
        time.sleep(1)
        print("You don't have that item and there is none in your current room")
    else:
        if key=='apple':
            time.sleep(1)
            print("You are watching a delicious apple")
            time.sleep(1)
            print("If you use this apple you will gain a random object from your inventory ")
        elif key=='knife':
            time.sleep(1)
            print('You are watching a sharp knife')
            time.sleep(1)
            print("It doesn't do much, but your wife would be happy if you bring it back home. ")
        elif key=="map":
            time.sleep(1)
            print("You are watching an old map.")
            time.sleep(1)
            print("When you find 4 pieces of it you will know the right room.")
        elif key=='box':
            time.sleep(1)
            print('You are watching a box of chocolates')
            time.sleep(1)
            print("All you can get from is some extra weight")
        elif key=='bullets':
            time.sleep(1)
            print('You are watching a rusty bullet')
            time.sleep(1)
            print('It can be used to shoot...')
            time.sleep(1)
            print("nothing because this is a child-friendly game")


def drop_item(key):
    playerInv[key]-=1
    print('the ',str(key),'is lost forever now')

def use_apple():
    if playerInv['apple']>=1:
        pinv=list(playerInv.keys())
        newitem=random.choice(pinv)
        playerInv[newitem]+=1
        time.sleep(1)
        print("Wow, you got a new ",str(newitem))
        playerInv['apple']-=1
        time.sleep(1)
        print("You now have only ",playerInv['apple']," now")
    else:
        time.sleep(1)
        print("You don't have any apples, go and search some")


def use_maps():
    if playerInv['map']>=4:
        time.sleep(1)
        print("The donuts are in the room ",str(rightroom),'!')
    else:
        time.sleep(1)
        print("You don't have enough pieces, go and search some")


def use_donuts():
    if playerInv['THE GOLEDN DONUTS']==1:
        time.sleep(1)
        print("You can now fulfill your destiny, enjoy them")
    else:
        time.sleep(1)
        print("Your adventure is not finished yet")
            
#player
playerInv={}
currentRoom=0

    
#some little talk to let the player know his task
print("Greetings!")
time.sleep(1)
print("Your name is Bob. ")
time.sleep(1)
print("Your sole purpose in life is to eat the GOLDEN DONUTS!!!")
time.sleep(1)
print("After years of research you found out they are hidden in the Great GOLDEN CASTLE ")
time.sleep(1)
print("I guess you know what you have to do now, if not you will figure something out")
time.sleep(1)
falsename=input("Enter your name: ")
time.sleep(1)
if falsename !="Bob":
    print("...")
    time.sleep(1)
    print("I just told you your name is Bob, please pay attention")
    time.sleep(1)
    print("Anyway, let's begin")
else:
    print("Oh, I see you are a clever adventurer")
    time.sleep(1)
    print("Let's begin")
    time.sleep(1)
time.sleep(1)
print("You enter in the Great GOLDEN CASTLE")
time.sleep(1)
print("You see 5 doors on your left and 5 doors on your right")
time.sleep(1)
print("You enter the first one on the left")

#main loop
while True:
    time.sleep(1)
    print("Do you wanna see a list of commands?")
    yn=input("y/n?")
    if yn=='y':
        time.sleep(1)
        print("'w' gets you in northen room")
        print("'s' gets you in the southern room")
        print("'d' gets you in the eastern room")
        print("'a' gets you in the western room ")
        print("'lookroom' gets you a list of items in your current room ")
        print("'look [ item ]' gets you a shot description of a item which is in your inventory or in the current room ")
        print("'drop [item]' drop a certain item which is in your inventory ")



