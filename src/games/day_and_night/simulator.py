from games.day_and_night.player import DayAndNightPlayer
from games.day_and_night.state import DayAndNightState
from games.game_simulator import GameSimulator


class DayAndNightSimulator(GameSimulator):

    def __init__(self, player1: DayAndNightPlayer, player2: DayAndNightPlayer, size: int):
        super(DayAndNightSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the day_and_night grid
        """
        self.__num_rows = size
        self.__num_cols = size

    def init_game(self):
        return DayAndNightState(self.__num_rows)

    def before_end_game(self, state: DayAndNightState):
        # ignored for this simulator
        pass

    def end_game(self, state: DayAndNightState):
        # ignored for this simulator
        pass
