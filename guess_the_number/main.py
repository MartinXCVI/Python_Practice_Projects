import random

range_top = input("Type a number: ")

if range_top.isdigit():
    range_top = int(range_top)

    if range_top <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a valid number next time.")
    quit()

random_num = random.randint(0, range_top)
guesses_num = 0

while True:
    guesses_num += 1
    user_guess = input("Make your guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_num:
        print("You did it!")
        break
    elif user_guess > random_num:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses_num, "guesses!")
