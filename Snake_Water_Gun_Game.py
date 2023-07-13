# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements or your own method. Do not create any fancy GUI. Use proper functions to check for win.

#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

# Create tuple

import random

print("\t\t This is snake,water,gun game ")
print("\t\t Enter 0 for Snake ")
print("\t\t Enter 1 for Water ")
print("\t\t Enter 2 for Gun")
print("\t\t  You have 6 round Whom will win more round wil be the winner")
print("\t\t Good Luck Hope You win but I knew,I will Win")

# tuple
Values=(0,1,2)
user=0
com=0
for i in range(1,6):
 print( "This is round {0}".format(i))
 print(" Computer is Thinking ")
 s=random.choice(Values)
 for r in range(0,1):
    K=int(input("Enter Your choice 0 1 2 "))
    print( "Computer choice is {0}".format(s))
    if K==s:
      print( "This  round {0} is draw\n".format(i))
    elif (K>=0 and K<=2 and s==0 and K==1):
            print( "This  round {0} is win by user\n".format(i))
            user=user+1
    elif (K>=0 and K<=2 and s==1 and K==0):
            print( "This  round {0} is win by computer\n".format(i))
            com=com+1
    elif (K>=0 and K<=2 and s==0 and K==2):
            print( "This  round {0} is win by user\n".format(i))
            user=user+1
    elif (K>=0 and K<=2 and s==2 and K==0):
            print( "This  round {0} is win by computer\n".format(i))
            com=com+1
    elif (K>=0 and K<=2 and s==2 and K==1):
            print( "This  round {0} is win by user\n".format(i))
            user=user+1
    elif (K>=0 and K<=2 and s==1 and K==2):
            print( "This  round {0} is win by computer\n".format(i))
            com=com+1
    else:
         print( "\t\t Invalid choice \n ")
         exit(0)


if(com<user):
  print("\t\t User Win Congratulation\n")
elif(com>user):
    print("\t\t Computer Win Congratulation\n")
else:
  print("Draw")

