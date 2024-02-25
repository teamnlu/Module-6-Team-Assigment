#This program make you guess a generated random number if not guess will ask to guess lower or higher
#Julian Torres, Beltran Kelly, Borders Stevaughn, Crosby cierra , Emmanuel Velazquez 
import random

while True:
    rand_num = random.randrange(1,11)
    
    guessed = False
    
    while not guessed:
        guess_num = int(input("Please guess a number between 1 and 10: "))
        
        if guess_num == rand_num:
            print("Well done! You guessed correctly.")
            guessed = True
        elif guess_num > rand_num:
            print("Guess lower!")
        else: 
            print("Guess higher!")
            
    play_again = input("Would you like to guess another number? (Y/N)").lower()       
    if play_again != "y":
        break
        
print("Bye!")
                

