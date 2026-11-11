from client import display_menu, get_menu_choice, display_game_results,display_game_history, display_satistics, get_number_of_rounds, get_player_name
from game_logic import start_game
from storage import save_game, load_game_history

def main():
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            player_name = get_player_name()
            rounds = get_number_of_rounds()
            game = start_game(player_name, rounds)
            display_game_results(game)
            if save_game(game):
                print("\nGame saved successfully!")

        elif choice == "2":
            history = load_game_history()
            display_game_history(history)

        elif choice == "3":
            history = load_game_history()
            display_satistics(history)

        elif choice == "4":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()