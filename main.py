from client import display_menu, get_menu_choice, display_game_results
from game_logic import start_game
from storage import save_game

def main():
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            player_name = input("Player name: ")
            rounds = int(input("Number of rounds: "))
            game = start_game(player_name, rounds)
            display_game_results(game)
            if save_game(game):
                print("\nGame saved successfully!")

        elif choice == "2":
            print("Viewing game history...")

        elif choice == "3":
            print("Viewing statistics...")

        elif choice == "4":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()