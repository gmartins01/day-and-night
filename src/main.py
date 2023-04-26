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
    print("ESTG IA Games Simulator")

    num_iterations = 1

    c4_simulations = [
        # uncomment to play as human
        # {
        #    "name": "Day and Night - Human VS Human",
        #    "player2": HumanDayAndNightPlayer("Human 1"),
        #    "player1": HumanDayAndNightPlayer("Human 2")
        # },
        {
            "name": "Day and Night - Human VS Greedy",
            "player1": HumanDayAndNightPlayer("Human"),
            "player2": GreedyDayAndNightPlayer("Greedy")
        },
        # {
        #     "name": "Minimax VS Random",
        #     "player1": MinimaxDayAndNightPlayer("Minimax"),
        #     "player2": RandomDayAndNightPlayer("Random")
        # },
        # {
        #     "name": "Minimax VS Greedy",
        #     "player1": MinimaxDayAndNightPlayer("Minimax"),
        #     "player2": GreedyDayAndNightPlayer("Greedy")
        # }
    ]

    for sim in c4_simulations:
        run_simulation(sim["name"], DayAndNightSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
