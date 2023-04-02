from typing import Optional

from games.day_and_night.action import DayAndNightAction
from games.day_and_night.result import DayAndNightResult
from games.state import State

BLK = -1
WHI = -2

class DayAndNightState(State):
    EMPTY_CELL = -1

    def __init__(self, size: int = 11):
        super().__init__()

        if size != 11:
            raise Exception("the number of rows and cols must be 11")

        """
        the dimensions of the board
        """
        self.__num_rows = size
        self.__num_cols = size

        """
        the grid
        """
        self.__grid = [
            [WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI],
            [BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK],
            [WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI],
            [BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK],
            [WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI],
            [BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK],
            [WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI],
            [BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK],
            [WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI],
            [BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK],
            [WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI,BLK,WHI]
        ]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def __check_winner(self, player):
        # check for 4 across
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row][col + 1] == player and \
                        self.__grid[row][col + 2] == player and \
                        self.__grid[row][col + 3] == player:
                    return True

        # check for 4 up and down
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player and \
                        self.__grid[row + 3][col] == player:
                    return True

        # check upward diagonal
        for row in range(3, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player and \
                        self.__grid[row - 3][col + 3] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player and \
                        self.__grid[row + 3][col + 3] == player:
                    return True

        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: DayAndNightAction) -> bool:
        col = action.get_col()
        row = action.get_row()

        # valid column
        if col < 0 or col >= self.__num_cols:
            return False

        # valid row
        if row < 0 or row >= self.__num_rows:
            return False

        # full column
        #if self.__grid[0][col] != DayAndNightState.EMPTY_CELL:
        #    return False

        # valid move
        if self.__grid[row][col] != WHI and self.__grid[row][col] != BLK:
            return False

        return True

    def update(self, action: DayAndNightAction):
        col = action.get_col()
        row = action.get_row()

        self.__grid[row][col] = self.__acting_player
    
        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

    def __display_cell(self, row, col):
        print({
                  0: ' B ',
                  1: ' W ',
                  BLK: '\033[1;40m   \033[0m',
                  WHI: '\033[1;47m   \033[0m'
              }[self.__grid[row][col]], end="")
    
    # def __display_cell(self, row, col):
    #     cell_value = self.__grid[row][col]
    #     if cell_value == BLK:
    #         print('\033[1;31m \033[0m', end="")
    #     elif cell_value == WHI:
    #         print('\033[47m \033[0m', end="")
    #     else:
    #         color = '\033[1;30m' if cell_value == BLK else '\033[1;37m'
    #         background_color = '\033[47m' if (row+col) % 2 == 0 else '\033[40m'
    #         print(f"{background_color}{color} {background_color}\033[0m,", end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print('  ', end="")
            if col >= 10:
                print('  ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("---", end="")
        print("-")

    # def display(self):
    #     print("  ", end="")
    #     self.__display_numbers()
    #     self.__display_separator()

    #     for row in range(0, self.__num_rows):
    #         if row < 10:
    #             print(row,' |', end="")
    #         if row >= 10:
    #             print(row,'|', end="")
    #         for col in range(0, self.__num_cols):
    #             self.__display_cell(row, col)
    #             print('|', end="")

    #         print("")
    #         self.__display_separator()
            
    #     print("  ", end="")
    #     self.__display_numbers()
    #     print("")

    def display(self):
        print("  ", end="")
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.__num_rows):
            if row < 10:
                print(row,' |', end="")
            if row >= 10:
                print(row,'|', end="")
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
                print('', end="")

            print("")
            
        print("  ", end="")
        self.__display_separator()
        self.__display_numbers()
        print("")
        

    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = DayAndNightState(self.__num_rows)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[DayAndNightResult]:
        if self.__has_winner:
            return DayAndNightResult.LOOSE if pos == self.__acting_player else DayAndNightResult.WIN
        if self.__is_full():
            return DayAndNightResult.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass

    def get_possible_actions(self):
        return list(filter(
            lambda action: self.validate_action(action),
            map(
                lambda pos: DayAndNightAction(pos),
                range(0, self.get_num_cols()))
        ))

    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
