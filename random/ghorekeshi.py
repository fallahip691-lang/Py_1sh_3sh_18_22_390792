




from random import *

members=[]


while True:
        name = input("family member").strip()
        if name in members:
           print("name is reapated")
        elif name=="exit":
                break

        else:
            members.append(name)
        

winners = []

if members:
    winner = choice(members)
    print("winner:", winner)
else:
    print("no members")