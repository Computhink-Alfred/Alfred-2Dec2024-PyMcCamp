# Write all your codes for Day 3 here.
# REMEMBER to change main.py to import this file.
# You can COMMENT out the previous task before going on to the next task
# userName = input("What is your name? ")
# userTitle = input("What is your title? ")
# userCommand = input("What command would you like to give? ")

# print(userTitle + " " + userName + " commands his students to " + userCommand)

# num1 = input("Enter the first number to add: ")
# num2 = input("Enter the second number to add: ")

# ans = str(int(num1) + int(num2))

# print(num1 + " + " + num2 + " = " + ans)


# numToMultiply = int(input("Enter the number to multiply: "))
# numOfMultiplication = int(input("How many times do you want to multiply? "))

# for i in range(1, numOfMultiplication + 1):
#     print(str(i) + " x " + str(numToMultiply) + " = " + str(i*numToMultiply))

# import random

# randNum = random.randint(1, 3)
# userAns = int(input("Guess a number: "))

# if userAns == randNum:
#     print("Congratulations! You have won $1 billion dollars!")
# elif userAns > randNum:
#     print("Womp womp, you guess too high")
# else:
#     print("Womp womp, you guess too low")

userAge = int(input("What is your age? "))

if userAge < 5:
    print("You are less than 5.")
elif userAge < 10:
    print("You are between 5 and 9 years old.")
else:
    print("You must be at least 10 years old.")