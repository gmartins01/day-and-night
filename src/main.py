from games.day_and_night.players.greedy import GreedyDayAndNightPlayer
from games.day_and_night.players.minimax import MinimaxDayAndNightPlayer
from games.day_and_night.players.random import RandomDayAndNightPlayer
from games.day_and_night.simulator import DayAndNightSimulator
from games.day_and_night.players.human import HumanDayAndNightPlayer
from games.game_simulator import GameSimulator

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator\n")
    print("Day and Night Game\n")
    while True:
        print("Choose the player 1:")
        
        print("1 - Human")
        print("2 - Computer (Easy)")
        print("3 - Computer (Medium)")
        print("4 - Computer (Hard)")
        print("0 - Exit")
        player1 = int(input())
        if player1 == 0:
            break
        print("Choose the player 2:")
        print("1 - Human")
        print("2 - Computer (Easy)")
        print("3 - Computer (Medium)")
        print("4 - Computer (Hard)")
        print("0 - Exit")
        player2 = int(input())
        if player2 == 0:
            break
        print("Enter the number of games:")
        num_iterations = int(input())
        if num_iterations == 0:
            break
        
        while True:
            board_size = int(input("Enter the board size: "))
            if board_size < 11 or board_size > 19 or board_size % 2 == 0:
                print("The size of the board must be an odd number between 11 and 19")
            else:
                break
            

        if player1 == 1:
            player1 = HumanDayAndNightPlayer("Human 1")
        elif player1 == 2:
            player1 = RandomDayAndNightPlayer("Random")
        elif player1 == 3:
            player1 = GreedyDayAndNightPlayer("Greedy")
        elif player1 == 4:
            player1 = MinimaxDayAndNightPlayer("Minimax")
        else:
            print("Invalid option")
            break
        if player2 == 1:
            player2 = HumanDayAndNightPlayer("Human 2")
        elif player2 == 2:
            player2 = RandomDayAndNightPlayer("Random")
        elif player2 == 3:
            player2 = GreedyDayAndNightPlayer("Greedy")
        elif player2 == 4:
            player2 = MinimaxDayAndNightPlayer("Minimax")
        else:
            print("Invalid option")
            break

        c4_simulations = [
            {
                "name": "Day and Night",
                "player1": player1,
                "player2": player2
            }
        ]
    #num_iterations = 10

    # c4_simulations = [
    #     # uncomment to play as human
    #     # {
    #     #    "name": "Day and Night - Human VS Human",
    #     #    "player2": HumanDayAndNightPlayer("Human 1"),
    #     #    "player1": HumanDayAndNightPlayer("Human 2")
    #     # },
    #     # {
    #     #     "name": "Day and Night - Random VS Greedy",
    #     #     "player1": RandomDayAndNightPlayer("Random"),
    #     #     "player2": GreedyDayAndNightPlayer("Greedy")
    #     # },
    #     # {
    #     #     "name": "Minimax VS Random",
    #     #     "player1": MinimaxDayAndNightPlayer("Minimax"),
    #     #     "player2": RandomDayAndNightPlayer("Random")
    #     # },
    #     {
    #         "name": "Minimax VS Greedy",
    #         "player1": MinimaxDayAndNightPlayer("Minimax"),
    #         "player2": GreedyDayAndNightPlayer("Greedy")
    #     }
    # ]

        for sim in c4_simulations:
            run_simulation(sim["name"], DayAndNightSimulator(sim["player1"], sim["player2"],board_size), num_iterations)


if __name__ == "__main__":
    main()
