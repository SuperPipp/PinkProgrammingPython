name = input("What is your name?\n")
print("Hello, {}!".format(name))
print("Welcome to Guessing Game")
score = 0
answer = input("What is the capital of Norway?\n")
if answer == "Oslo":
    print("True")
    score = score +1
else:
    print("False")
answer = input("Do you like Norway?\n")
if answer == "Yes":
    print("Wonderful!")
elif answer == "No":
    print("Too bad")
else:
    print("I'll accept it for now")
answer = input("What is 2+3?\n")
if answer == "5":
    print("True")
    score = score +1
else:
    print("False")
answer = input("How many primary colours are there?\n")
if answer == "3":
    print("True, well done!")
    score = score +2
else:
    print("False")
answer = input("What season is the warmest?\n")
if answer == "Summer":
    score = score +1
elif answer == "Spring":
    print("So close, but wrong")
else:
    print("False")
print("Thank you for playing")
print("Score:")