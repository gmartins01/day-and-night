from random import randint

from games.day_and_night.action import DayAndNightAction
from games.day_and_night.player import DayAndNightPlayer
from games.day_and_night.state import DayAndNightState
from games.state import State


class RandomDayAndNightPlayer(DayAndNightPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: DayAndNightState):
        return DayAndNightAction(randint(0, state.get_num_rows()),randint(0, state.get_num_cols()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
