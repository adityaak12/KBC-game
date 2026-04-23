import random

print("selact number in between 1 to 100")

number = random.randint(1,100)
attempts = 0

while True:
    
    guess=int(input("Enter your guess:-"))
    attempts += 1

    if guess == number :
        print("your guess is corrrect")
        print("your guess in",attempts,"attempts")
        break

    elif guess > number:
        print("Is too high")

    else :
        print("IS too low")