from games.day_and_night.action import DayAndNightAction
from games.day_and_night.player import DayAndNightPlayer
from games.day_and_night.state import DayAndNightState


class HumanDayAndNightPlayer(DayAndNightPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: DayAndNightState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                return DayAndNightAction(int(input(f"Player {state.get_acting_player()}, choose a row: ")),
                                         int(input(f"Player {state.get_acting_player()}, choose a column: ")))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: DayAndNightState):
        # ignore
        pass

    def event_end_game(self, final_state: DayAndNightState):
        # ignore
        pass
