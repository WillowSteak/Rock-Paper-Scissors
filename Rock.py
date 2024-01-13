# asking for input
choice = input("Rock (0) Paper(1) Scissors(2)?\n")
# we have to specify we are importing random to enable the use of random function
import random
# define a random value between 0-2 to value named rand
rand = random.randint(0, 2)

# cause and affect of user input or choice to rand value
if choice == '0':
    print("Rock")
    if rand == 0:
        print("Computer chose: Rock")
        print("It's a draw!")
    if rand == 1:
        print("Computer chose: Paper")
        print("You lose!")
    if rand == 2:
        print("Computer chose: Scissors")
        print("You win!")
if choice == '1':
    print("Paper")
    if rand == 0:
        print("Computer chose: Rock")
        print("You win!")
    if rand == 1:
        print("Computer chose: Paper")
        print("It's a draw!")
    if rand == 2:
        print("Computer chose: Scissors")
        print("You lose!")
if choice == '2':
    print("Scissors")
    if rand == 0:
        print("Computer chose: Rock")
        print("You lose!")
    if rand == 1:
        print("Computer chose: Paper")
        print("You win!")
    if rand == 2:
        print("Computer chose: Scissors")
        print("It's a draw!")
else:
    print("You didnt choose a value.......")
print ("Thank you for playing! :)")
        