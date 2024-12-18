import random
def number_guessing_game():
    while True: # 1 dan 100gacha bulgan sonlardan
        number_to_guess = random.randint (1,100)
        attempts=10
        print( "Guess the number between 1 and 100. You have 10 attempts!")


        while attempts > 0:
            try:
                # Take input from the player
                guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
                
                if guess < number_to_guess:
                    print("Too low!")
                elif guess > number_to_guess:
                    print("Too high!")
                else:
                    print("You guessed it right!")
                    break
                
                attempts -= 1
            except ValueError:
                print("Please enter a valid number.")

        if attempts == 0:
            print("You lost. The correct number was:", number_to_guess)
        
        # Ask to play again
        play_again = input("Want to play again? (Y/YES/y/yes/ok): ").strip().lower()
        if play_again not in ['y', 'yes', 'ok']:
            print("Thanks for playing!")
            break

# Start the game
number_guessing_game()


        
