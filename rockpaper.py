import random


def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user, computer):
    """Determine the winner of the round."""
    if user == computer:
        return "tie"

    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if winning_combinations[user] == computer:
        return "user"
    else:
        return "computer"


def display_score(user_score, computer_score):
    """Display the current score."""
    print("\n" + "-" * 35)
    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")
    print("-" * 35)


def play_game():
    """Run the Rock Paper Scissors game."""

    user_score = 0
    computer_score = 0

    print("=" * 45)
    print("        ROCK PAPER SCISSORS GAME")
    print("=" * 45)
    print("Choose: Rock, Paper, or Scissors")
    print("Rock > Scissors")
    print("Scissors > Paper")
    print("Paper > Rock")
    print("=" * 45)

    while True:

        # Get user input
        user_choice = input(
            "\nEnter your choice: "
        ).strip().lower()

        # Validate input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice. Please try again.")
            continue

        # Generate computer choice
        computer_choice = get_computer_choice()

        # Display choices
        print(f"\nYou chose      : {user_choice.capitalize()}")
        print(f"Computer chose : {computer_choice.capitalize()}")

        # Determine winner
        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            print("🎉 You win this round!")
            user_score += 1

        elif winner == "computer":
            print("💻 Computer wins this round!")
            computer_score += 1

        else:
            print("🤝 It's a tie!")

        # Display score
        display_score(user_score, computer_score)

        # Ask to play again
        while True:
            play_again = input(
                "Do you want to play again? (yes/no): "
            ).strip().lower()

            if play_again in ["yes", "no"]:
                break

            print("❌ Please enter 'yes' or 'no'.")

        if play_again == "no":
            break

    # Final result
    print("\n" + "=" * 45)
    print("              FINAL RESULT")
    print("=" * 45)

    display_score(user_score, computer_score)

    if user_score > computer_score:
        print("🏆 Congratulations! You are the overall winner!")
    elif computer_score > user_score:
        print("💻 Computer is the overall winner!")
    else:
        print("🤝 The overall game is a tie!")

    print("\nThank you for playing! 👋")


# Start the game
if __name__ == "__main__":
    play_game()