print("Welcome to a game of Rock, paper, Scissors wherein you'll be up against your very own computer! \nIf you want to exit the game, press 'x' anytime. Now let's play!")
print("\n")
name=str(input("User's First Name: ")).upper()
lname=str(input("User's Last Name: ")).upper()
print("\n")
import random

move=['1','2','3']

while True:
    
    choice=str(input("Pick your choice [1=ROCK, 2=PAPER, 3=SCISSORS]: "))
    if choice=='x':
        break
    compChoice=random.choice(move)


    if choice=='1':
        (choice)="ROCK"
    elif choice=='2':
        (choice)="PAPER"
    elif choice=='3':
        (choice)="SCISSORS"
    else:
        print("Invalid")
        break



    if compChoice=='1':
        compChoice="ROCK"
    elif compChoice=='2':
        compChoice="PAPER"
    else:
        compChoice="SCISSORS"


    print(name,lname,"chose",choice,end="; ")
    print("Computer chose",compChoice)

    if choice==compChoice:
        print("It's a tie! Try again! :D")
    elif choice=="ROCK" and compChoice=="SCISSORS":
        print("You win! ^_^")
    elif choice=="PAPER" and compChoice=="ROCK":
        print("You win! ^_^")
    elif choice=="SCISSORS" and compChoice=="PAPER":
        print("You win! ^_^")
    else:
        print("You lose!",":P")

    print("\n")
            
    





 
