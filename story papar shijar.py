import random

a = "Stone"
b="papar"
u="scissors"

choice=["a","b","u"]
print("a=Stone, b=papar, u=scissors")
print("This is a game of stone,papar,scissors")

i=input("Selact a one of the between(stone,papar,scissors):-")

c=random.choice(choice)

if c == i :
   print("this is tie")
elif (i == "a"and c =="u") or \
     (i == "u" and c == "b") or \
     (i == "b"and c == "a") :
     print("YOU WIN")

elif (i == "a"and c =="b") or \
     (i == "u" and c == "a") or \
     (i == "b"and c == "u") :
    print("YOU LOSS")

else:
    print("invilid input")