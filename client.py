def display_menu():
    print("================================")
    print("             ROLL DICE")
    print("================================")
    print("1. Start New Game 🎲")
    print("2. View Game History")
    print("3. View Statistics")
    print("4. Exit")
    print("================================")


def get_menu_choice():
    while True:
        choise = input("Enter your choise: ")
        if choise in ["1", "2", "3", "4"]:
            return choise
        print("Invalide choise, please enter between 1 to 4")


def display_game_results(game):
    print("\n================================")
    print("          NEW GAME")
    print("================================")
    
    for result in game["result"]:
        print(f"\n----------- ROUND {result['round']} -----------")
        
        print(f"{game['player_name']}:    🎲   {result['player_dice']}")
        print(f"computer:   🎲  {result['computer_dice']}")
        
        if result["winner"] == "Player":
            print(f"{game['player_name']} wins this round!")
            
        elif result["winner"] == "computer":
            print("Computer win this round!")
        
        else:
            print("its a draw!")

    print("\n================================")
    print("          GAME OVER")
    print("================================")
    
    print(f"\n{game['player_name']}:  🎲  {game['player_score']} points")
    print(f"Computer: 🎲 {game['computer_score']} points")
    
    if game["winner"] == "Player":
        print(f"\nWINNER: {game['player_name']}!")
    elif game["winner"] == "Computer":
        print(f"WINNER: Computer!")
    else:
        print("\nGAME RESULT: Draw!")
        
        

def display_game_history(history):
    print("\n================================")
    print("          GAME HISTORY")
    print("================================")
    
    if not history:
        print("no games found.")
        return
        
    for index, game in enumerate(history, start=1):
        print(f"\n---------- GAME {index} ----------")
        
        print(f"Player: {game['player_name']}")
        print(f"Rounds: {game['rounds']}")
        print(f"Player Score: {game['player_score']}")
        print(f"Computer Score: {game['computer_score']}")
        
        if game["winner"] == "Player":
            print(f"Winner: {game['player_name']}")
        elif game["winner"] == "Computer":
            print("Winner: Computer")
        else:
            print("Winner: Draw")
            


def display_satistics(history):
    total_games = len(history)
    player_wins = 0
    computer_wins = 0
    draws = 0
    for game in history:
        if game["winner"] == "Player":
            player_wins += 1
        elif game["winner"] == "Computer":
            computer_wins += 1
        else:
            draws += 1
    if total_games > 0:
        player_percentage = (player_wins /total_games) *100
        computer_percentage = (computer_wins / total_games)*100
    else:
        player_percentage = 0
        computer_percentage =0
    
    
    print("\n================================")
    print("          STATISTICS")
    print("================================")
    
    print(f"Total games: {total_games}")
    print(f"Player wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Draws: {draws}")
           
    print(f"Player win rate: {player_percentage:.1f}%")
    print(f"Computer win rate: {computer_percentage:.1f}%")
    
    
# validtion , name  not empty, up to 10 rounds
    
def get_player_name():
    while True:
        name = input("Player name: ").strip()

        if name:
            return name

        print("Name cannot be empty. Please try again.")
        
        
        
def get_number_of_rounds():
    while True:
        try:
            rounds = int(input("Number of rounds: "))
            if 1 <= rounds <= 10:
                return rounds
            print("Please choose between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")