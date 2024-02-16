import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

def roll_dice():
    return random.randint(1, 6)

def player_turn(player):
    print(f"It's {player.name}'s turn.")
    input("Press Enter to roll the dice...")

    dice = roll_dice()
    print(f"{player.name} rolled a {dice}.")

    if dice == 1:
        print("You rolled a 1. No points earned this turn.")
        return 0

    return dice

def pig_game(num_players):
    players = [Player(input(f"Enter the name of player {i+1}: ")) for i in range(num_players)]
    while True:
        for player in players:
            turn_score = 0
            while True:
                roll = player_turn(player)
                if roll == 0:
                    break
                turn_score += roll

                print(f"Turn total: {turn_score}")
                choice = input("Roll again (r) or hold (h)? ").lower()
                if choice != 'r':
                    player.add_score(turn_score)
                    print(f"{player.name}'s total score is now {player.score}")
                    break

                if player.score + turn_score >= 50:
                    print(f"Congratulations! {player.name} wins with {player.score + turn_score} points!")
                    return

            if player.score >= 50:
                print(f"Congratulations! {player.name} wins with {player.score} points!")
                return

if __name__ == "__main__":
    num_players = int(input("Enter the number of players (1-4): "))
    num_players = min(max(num_players, 1), 4)  # Limit number of players between 1 and 4
    pig_game(num_players)
