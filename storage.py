import json

def load_game_history():
    try:
        with open("game_history.json", "r") as file:
            history = json.load(file)
        return history
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        print("ERRORR: game history file is invalid")
        return []
    
    
    
def save_game(game):
    history = load_game_history()
    history.append(game) 
    
    with open("game_history.json", "w") as file:
        json.dump(history, file, indent=4)
