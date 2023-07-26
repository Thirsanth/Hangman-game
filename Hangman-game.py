import random
lst=["COMPUTER","LAPTOP","TABLET","PYTHON","PROGRAMMIG","JAVA"]
user_name=input("Enter your name:")
print('-'*120)
print("Welcome to the HangMan game",user_name.upper())
print('-'*120)
print("YOU WILL HAVE 11 GUESSES TO GUESS THE WORD AND IF YOU ARE UNABLE TO GUESS THE WORD THEN YOU WILL BE ELIMINATED")
print('-'*120)
rn_selected=random.choice(lst)
guess=''
turns=11
while turns>0:
    failed=0
    for i in rn_selected:
        if i in guess:
            print(i,end="")
        else:
            print(' _ ',end="")
            failed+=1
    if failed==0:
        print("\nYou have won")
        break
    guesses=input("\n\nGuess a letter:")
    guesses=guesses.upper()
    guess+=guesses
    if guesses not in rn_selected:
        turns-=1
        print("\nWrong")
        print("\nYou have",turns,"left")
        if turns==0:
            print("\nYou have lost")

