from random import choice
from games.day_and_night.action import DayAndNightAddAction
from games.day_and_night.action import DayAndNightMoveAction
from games.day_and_night.player import DayAndNightPlayer
from games.day_and_night.state import DayAndNightState
from games.state import State


class GreedyDayAndNightPlayer(DayAndNightPlayer):

    def __init__(self, name):
        super().__init__(name)
        self.add_turn_counter = 0
        self.move_turn_counter = 0

    def get_action(self, state: DayAndNightState):
        grid = state.get_grid()
        selected_row_from = None
        selected_col_from = None
        selected_row_to = None
        selected_col_to = None
        max_count = 0
        
        #state.display()
        possible_add_actions = state.get_possible_add_actions()
        possible_move_actions = state.get_possible_move_actions()
        if self.add_turn_counter <= 3 and len(possible_add_actions) > 0:
            for row in range(0, state.get_num_rows()):
                for col in range(0, state.get_num_cols()):
                    if not state.validate_action(DayAndNightAddAction(col,row)):
                        continue

                    count = 0
                    for row in range(0, state.get_num_rows()):
                        for col in range(0, state.get_num_cols()):
                            if grid[row][col] == int(str(state.EMPTY_BLK) + str(self.get_current_pos())) or\
                                    grid[row][col] == int(str(state.EMPTY_WHI) + str(self.get_current_pos())):
                                count += 1
                            if selected_col_to is None or count > max_count or (count == max_count and choice([False, True])):
                                #print("aqui1")
                                selected_col_to = col
                                max_count = count

                            if selected_row_to is None or count > max_count or (count == max_count and choice([False, True])):
                                #print("aqui2")
                                selected_row_to = row
                                max_count = count

            self.add_turn_counter += 1
            return DayAndNightAddAction(selected_row_to,selected_col_to)
        
        elif self.move_turn_counter <= 2 and len(possible_move_actions) > 0:
            for row in range(0, state.get_num_rows()):
                for col in range(0, state.get_num_cols()):
                    if not state.validate_action(DayAndNightAddAction(col,row)):
                        continue

                    count = 0
                    for row in range(0, state.get_num_rows()):
                        for col in range(0, state.get_num_cols()):
                            if grid[row][col] == int(str(state.EMPTY_BLK) + str(self.get_current_pos())) or\
                                    grid[row][col] == int(str(state.EMPTY_WHI) + str(self.get_current_pos())):
                                count += 1
                                print("count: ", count)
                            if selected_col_from is None or count > max_count or (count == max_count and choice([False, True])):
                                #print("aqui1")
                                selected_col_from = col
                                max_count = count

                            if selected_row_from is None or count > max_count or (count == max_count and choice([False, True])):
                                #print("aqui2")
                                selected_row_from = row
                                max_count = count
                            if selected_col_to is None or count > max_count or (count == max_count and choice([False, True])):
                                #print("aqui1")
                                selected_col_to = col
                                max_count = count

                            if selected_row_to is None or count > max_count or (count == max_count and choice([False, True])):
                                #print("aqui2")
                                selected_row_to = row
                                max_count = count

            self.move_turn_counter += 1
            return DayAndNightMoveAction(selected_row_from,selected_col_from,selected_row_to,selected_col_to)
        else:
            self.add_turn_counter = 0
            self.move_turn_counter = 0
            return None

        if selected_col_to is None or selected_row_to is None:
            raise Exception("There is no valid action")

        


    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass