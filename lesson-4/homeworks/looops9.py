def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    winning_score = 5

    print("Welcome to Rock, Paper, Scissors!")
    print("First to 5 points wins. Good luck!\n")

    while player_score < winning_score and computer_score < winning_score:
        computer_choice = random.choice(choices)
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        print(f"Computer chose: {computer_choice}")
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Scores -> You: {player_score}, Computer: {computer_score}\n")

    if player_score == winning_score:
        print("Congratulations! You won the match!")
    else:
        print("The computer won the match. Better luck next time!")

# Start the game
rock_paper_scissors()
