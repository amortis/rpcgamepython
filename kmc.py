def check1(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
def check(n):
    if check1(n) == True:
        n = int(n)
        if n>=0 and n<=2:
            return True
        else:
            return "Please choice the correct number"
    else:
        while check1(n) != True:
            return "Please type the integer"
import random
print("Hello! Welcome to game: 'Rock-paper-scissors'")
print("You will battle with computer")
user1 = input('Now, what do you choose. Type 0 for Rock, 1 for paper, 2 for scissors. ')
while check(user1)!= True:
    print(check(user1))
    user1 = input("Try to type again ")
user = int(user1)
comp = random.randint(0,2)
knc = ['Rock', "Paper", 'Scissors']
comp1 = knc[comp]
print(f'Your choice : {knc[user]}')
print(f"Computer's choice : {comp1}")
if comp==user:
    print("It's a draw")
elif (comp == 0 and user == 2) or (comp==1 and user==0) or (comp == 2 and user == 1):
    print("You're lost. Don't get upset and try again!")
elif (comp == 0 and user == 1) or (comp==1 and user==2) or (comp == 2 and user == 0):
    print("Congratulations! You won!")


