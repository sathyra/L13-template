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

if(UserInput == SystemInput):
   print("Game is draw")
elif (UserInput == 2 and SystemInput == 1) or (UserInput == 1 and SystemInput == 0) or (UserInput == 0 and SystemInput == 2):
   print("User is the winner")
else:
   print("System is winner")