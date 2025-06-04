import random
from enum import Enum, auto

class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    def __str__(self):
        return self.name.capitalize()

def interpret_input(user_input):
    lookup = {'r': Move.ROCK, 'p': Move.PAPER, 's': Move.SCISSORS}
    return lookup.get(user_input.lower())

def determine_winner(player, computer):
    if player == computer:
        return "draw"
    if (
        (player == Move.ROCK and computer == Move.SCISSORS) or
        (player == Move.SCISSORS and computer == Move.PAPER) or
        (player == Move.PAPER and computer == Move.ROCK)
    ):
        return "player"
    return "computer"

def get_random_move():
    return random.choice(list(Move))

def display_scores(scores):
    print(f"🏆 Scores → You: {scores['player']} | Computer: {scores['computer']} | Draws: {scores['draws']}\n")

def main():
    print("=== Let's play Rock, Paper, Scissors! ===")
    print("Type 'r' for Rock, 'p' for Paper, 's' for Scissors. 'q' to quit.\n")

    scores = {"player": 0, "computer": 0, "draws": 0}

    while True:
        user_input = input("Your move [r/p/s/q]: ").strip()
        if user_input.lower() == 'q':
            print("👋 Thanks for playing!")
            break

        player_move = interpret_input(user_input)
        if not player_move:
            print("❌ Invalid input. Try again.")
            continue

        computer_move = get_random_move()
        print(f"🧠 Computer chose: {computer_move}")

        outcome = determine_winner(player_move, computer_move)
        if outcome == "draw":
            print("😐 It's a draw!")
            scores["draws"] += 1
        elif outcome == "player":
            print("🎉 You win!")
            scores["player"] += 1
        else:
            print("💻 Computer wins!")
            scores["computer"] += 1

        display_scores(scores)

if __name__ == "__main__":
    main()
