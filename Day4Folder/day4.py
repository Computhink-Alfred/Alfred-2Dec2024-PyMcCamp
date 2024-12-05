# Write all your codes for Day 4 here.
# REMEMBER to change main.py to import this file.
# You can COMMENT out the previous task before going on to the next task
# print("hello from day4")

# password = input("Please enter your password: ")
# counter = 1

# while counter < 5:
#     if password != "Alfred":
#         print("You have tried " + str(counter) + " times." )
#         password = input("Try again: ")
#         counter = counter + 1
#     else:
#         break

# if counter >= 5:
#     print("You are locked out")
# else:
#     print("You have successfully logged in")

userAns = input("What is opposite of black? ")
counter = 1

while userAns != "white":
    if counter == 2:
        print("Answer starts with 'w'")
    elif counter == 4:
        print("Answer is 5 letters long")
    elif counter > 6:
        print("It is a lack of colour")
    userAns = input("What is opposite of black? ")
    counter = counter + 1

print("You are correct!")