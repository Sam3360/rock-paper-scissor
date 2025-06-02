import random

def play_rock_paper_scissors():
    
    choices = ["rock", "paper", "scissors"]
    
    
    computer_choice = random.choice(choices)
    
    player_choice = ""
    while player_choice not in choices:
        print("Rock")
        print("Paper")
        print("Scissor")
        print("Shoot")
        player_choice = input("Choose rock, paper, or scissors: ").lower().strip()
        if player_choice not in choices:
            print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")

    print(f"\nYou chose: {player_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("Computer wins!")
    print("-" * 30)

def main():
    
    print("--- Welcome to Rock, Paper, Scissors! ---")
    
    while True:
        play_rock_paper_scissors()
        
        play_again = input("Play again? (yes/no): ").lower().strip()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
