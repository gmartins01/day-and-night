from games.day_and_night.players.greedy import GreedyDayAndNightPlayer
from games.day_and_night.players.minimax import MinimaxDayAndNightPlayer
from games.day_and_night.players.random import RandomDayAndNightPlayer
from games.day_and_night.simulator import DayAndNightSimulator
from games.day_and_night.players.human import HumanDayAndNightPlayer
from games.game_simulator import GameSimulator
from games.day_and_night.player import DayAndNightPlayer

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()

def main():
    player1 = None
    player2 = None
    print("ESTG IA Games Simulator\n")
    print("----- Day and Night -----\n")
    print("Author: Gonçalo Martins Nº24512\n")
    print("Rules: https://www.boardspace.net/dayandnight/english/rules.html\n")

    while player1!=0 or player2!=0:
        while True:
            print("Choose the player 1:")
            
            print("1 - Human")
            print("2 - Computer (Easy)")
            print("3 - Computer (Medium)")
            print("4 - Computer (Hard)")
            print("0 - Exit")
            player1 = int(input())

            if player1 == 0:
                exit()
            elif player1 == 1:
                player1 = HumanDayAndNightPlayer("Human 1")
                break
            elif player1 == 2:
                player1 = RandomDayAndNightPlayer("Easy 1")
                break
            elif player1 == 3:
                player1 = GreedyDayAndNightPlayer("Medium 1")
                break
            elif player1 == 4:
                player1 = MinimaxDayAndNightPlayer("Hard 1")
                break
            else:
                print("Invalid option")

        while True:    
            print("Choose the player 2:")
            print("1 - Human")
            print("2 - Computer (Easy)")
            print("3 - Computer (Medium)")
            print("4 - Computer (Hard)")
            print("0 - Exit")
            player2 = int(input())
            

            if player2 == 0:
                exit()
            elif player2 == 1:
                player2 = HumanDayAndNightPlayer("Human 2")
                break
            elif player2 == 2:
                player2 = RandomDayAndNightPlayer("Easy 2")
                break
            elif player2 == 3:
                player2 = GreedyDayAndNightPlayer("Medium 2")
                break
            elif player2 == 4:
                player2 = MinimaxDayAndNightPlayer("Hard 2")
                break
            else:
                print("Invalid option")
                
        while True:
            num_iterations = int(input("Enter the number of games: "))
            if num_iterations == 0:
                exit()
            else:
                break
        
        while True:
            board_size = int(input("Enter the board size: "))
            if board_size < 11 or board_size > 19 or board_size % 2 == 0:
                print("The size of the board must be an odd number between 11 and 19")
            else:
                break
                
        c4_simulations = [
            {
                "name": "Day and Night",
                "player1": player2,
                "player2": player1
            }
        ]

        for sim in c4_simulations:
            run_simulation(sim["name"], DayAndNightSimulator(sim["player1"], sim["player2"],board_size), num_iterations)
    

   
if __name__ == "__main__":
    main()
