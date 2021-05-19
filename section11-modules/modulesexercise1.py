import sys
import random

# taking the args into parameter
first_parameter = int(sys.argv[1])
second_parameter = int(sys.argv[2])

# generate a number from 1-10
gennum = random.randint(first_parameter, second_parameter)


print(gennum)
while True:
# input from user?
    try:
        num = int(input(f"Guest the number from {first_parameter} to {second_parameter}? "))
        if first_parameter < num < second_parameter:
            if gennum == num: 
                print("Your guess is right!!!!!")
                break

# check if number right guess. Otherwise, ask again.
    except ValueError:
        print("Please input your number again.")