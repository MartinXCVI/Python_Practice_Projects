print("Welcome to the quiz game!")

userInput = input("Do you want to start to playing? ").lower()

if userInput != "yes":
    quit()

print("Okay, let's play :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does WWW stand for? ").lower()
if answer == "world wide web":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of France? ").lower()
if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does NASA stand for? ").lower()
if answer == "national aeronautics and space administration":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who did invent the alternating current power? ").lower()
if answer == "nikola tesla":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str(score / 5 * 100) + " %.")
