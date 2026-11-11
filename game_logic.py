import random

def roll_dice():
    dice = random.randint(1,6)
    return dice



def calculate_winner(player_score, computer_score):
    if player_score > computer_score:
        return "Player"
    elif computer_score > player_score:
        return "Computer"
    else:
        return "Draw"


def play_round():
    player_dice = roll_dice()
    computer_dice = roll_dice()
    winner = calculate_winner(player_dice, computer_dice)
    round_result = {
        "player_dice": player_dice,
        "computer_dice": computer_dice,
        "winner": winner
    }
    return round_result


def start_game(player_name, rounds):
    player_score = 0
    computer_score = 0
    result = []
    for round_number in range(1, rounds +1):
        round_result = play_round()
        
        round_result["round"] = round_number
        result.append(round_result)
        
        if round_result["winner"] == "Player":
            player_score += 1
        elif round_result["winner"] == "Computer":
            computer_score += 1
            
    Winner = calculate_winner(player_score, computer_score)
    game = {
        "player_name": player_name,
        "rounds": rounds,
        "player_score": player_score,
        "computer_score": computer_score,
        "winner": Winner,
        "result": result
    }
    return game

