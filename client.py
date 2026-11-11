def display_menu():
    print("================================")
    print("             ROLL DICE")
    print("================================")
    print("1. Start New Game")
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
        
        print(f"{game['player_name']}:       {result['player_dice']}")
        print(f"computer:     {result['computer_dice']}")
        
        if result["winner"] == "Player":
            print(f"{game['player_name']} wins this round!")
            
        elif result["winner"] == "computer":
            print("Computer win this round!")
        
        else:
            print("its a draw!")

    print("\n================================")
    print("          GAME OVER")
    print("================================")
    
    print(f"\n{game['player_name']}:    {game['player_score']} points")
    print(f"Computer: {game['computer_score']} points")
    
    if game["winner"] == "Player":
        print(f"\nWINNER: {game['player_name']}!")
    elif game["winner"] == "Computer":
        print(f"WINNER: Computer!")
    else:
        print("\nGAME RESULT: Draw!")