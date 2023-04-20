from random import choice
from games.day_and_night.action import DayAndNightAddAction
from games.day_and_night.action import DayAndNightMoveAction
from games.day_and_night.player import DayAndNightPlayer
from games.day_and_night.state import DayAndNightState
from games.state import State


class GreedyDayAndNightPlayer(DayAndNightPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: DayAndNightState):
        possible_add_actions = state.get_possible_add_actions()
        possible_move_actions = state.get_possible_move_actions()
        grid = state.get_grid()
        max_count = 0

        selected_row_from = None
        selected_col_from = None
        selected_row_to = None
        selected_col_to = None

        for row in range(0, state.get_num_rows()):
            for col in range(0, state.get_num_cols()):
                if not state.validate_add_action(DayAndNightAddAction(col,row)):
                    continue

                count = 0
                for row in range(0, state.get_num_rows()):
                    if grid[row][col] == self.get_current_pos():
                        count += 1

                    if selected_col_from is None or count > max_count or (count == max_count and choice([False, True])):
                        selected_col_from = col
                        max_count = count

                    if selected_row_from is None or count > max_count or (count == max_count and choice([False, True])):
                        selected_row_from = row
                        max_count = count
        
        for row in range(0, state.get_num_rows()):
            for col in range(0, state.get_num_cols()):
                if not state.validate_move_action(DayAndNightMoveAction(col,row)):
                    continue

                count = 0
                for row in range(0, state.get_num_rows()):
                    if grid[row][col] == self.get_current_pos():
                        count += 1

                    if selected_col_to is None or count > max_count or (count == max_count and choice([False, True])):
                        selected_col_to = col
                        max_count = count

                    if selected_row_to is None or count > max_count or (count == max_count and choice([False, True])):
                        selected_row_to = row
                        max_count = count
        
        if selected_col_to is None or selected_row_to is None:
            raise Exception("There is no valid action")


        #select a add move or move action
        if choice([True, False]):
            return DayAndNightAddAction(selected_col_to,selected_row_to)
        else:
            return DayAndNightMoveAction(selected_col_to,selected_row_to)
        
    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
