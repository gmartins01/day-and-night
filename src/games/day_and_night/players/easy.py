from random import randint

from games.day_and_night.action import DayAndNightAddAction, DayAndNightMoveAction
from games.day_and_night.player import DayAndNightPlayer
from games.day_and_night.state import DayAndNightState
from games.state import State


class EasyDayAndNightPlayer(DayAndNightPlayer):

    def __init__(self, name):
        super().__init__(name)
        self.add_turn_counter = 0
        self.move_turn_counter = 0

    def get_action(self, state: DayAndNightState):
        if self.add_turn_counter < 3:
            # Generate a random position for the Add action
            row = randint(0, state.get_num_rows() - 1)
            col = randint(0, state.get_num_cols() - 1)
            self.add_turn_counter += 1
            return DayAndNightAddAction(row, col)
        elif self.move_turn_counter < 2:
            while True:
                # Generate a random position for the Move action
                row_from = randint(0, state.get_num_rows() - 1)
                col_from = randint(0, state.get_num_cols() - 1)
                row_to = randint(0, state.get_num_rows() - 1)
                col_to = randint(0, state.get_num_cols() - 1)
                move_action= DayAndNightMoveAction(row_from, col_from, row_to, col_to)
                if state.validate_move_action(move_action):
                        self.move_turn_counter += 1
                        return move_action
        else:
            # Reset the turn counters
            self.add_turn_counter = 0
            self.move_turn_counter = 0
            # If all turns are completed, return None to signify the end of the player's turn
            return None
        
    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
