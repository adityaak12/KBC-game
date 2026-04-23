import random

choice=["stone","paper","scissors"]

print("This is a game of stone,papar,scissors")

i=input("Selact a one of the between(stone,papar,scissors):-")

c=random.choice(choice)

if c == i :
   print("this is tie")
elif ("i == stone "and"u == scissors") or \
     ("i == scissors"and"u == papar") or \
     ("i == papar"and"u == scissors") :
     print("YOU WIN")

elif c in choice :
    print("YOU LOSS")

else:
    print("invilid input")