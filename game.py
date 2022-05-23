import random
print("Let's play the Rock, Paper and Scissors game")
print('About the Game - 0: Rock, 1: Paper, 2: Scissors')
print('Rules of the Game : \n Rock smashes scissors  \n Paper covers rock \n Scissors cut paper.')
print('User please enter the value:')

#To understand typecasting please refer to Test Case-1
UserInput = int(input("Enter a choice (0: Rock, 1: Paper, 2: Scissors): "))


print('System entered the value:')
SystemInput = random.randint(0, 2)
print(SystemInput)

#conditional statement

