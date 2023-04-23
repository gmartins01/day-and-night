from typing import Optional

from games.day_and_night.action import DayAndNightAction
from games.day_and_night.action import DayAndNightAddAction
from games.day_and_night.action import DayAndNightMoveAction
from games.day_and_night.result import DayAndNightResult
from games.state import State

BLK = -1
WHI = -2

class DayAndNightState(State):
    EMPTY_CELL = -1
    EMPTY_BLK = -1
    EMPTY_WHI = -2

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
        player_on_black = int(str(BLK) + str(player))
        player_on_white = int(str(WHI) + str(player))
        # check for 5 across
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 4):
                if (self.__grid[row][col] == player_on_white or self.__grid[row][col] == player_on_black) and \
                        (self.__grid[row][col + 1] == player_on_white or self.__grid[row][col + 1] == player_on_black) and \
                        (self.__grid[row][col + 2] == player_on_white or self.__grid[row][col + 2] == player_on_black) and \
                        (self.__grid[row][col + 3] == player_on_white or self.__grid[row][col + 3] == player_on_black) and \
                        (self.__grid[row][col + 4] == player_on_white or self.__grid[row][col + 4] == player_on_black):
                    return True

        # check for 5 up and down
        for row in range(0, self.__num_rows - 4):
            for col in range(0, self.__num_cols):
                if (self.__grid[row][col] == player_on_white or self.__grid[row][col] == player_on_black) and \
                        (self.__grid[row + 1][col] == player_on_white or self.__grid[row + 1][col] == player_on_black) and \
                        (self.__grid[row + 2][col] == player_on_white or self.__grid[row + 2][col] == player_on_black) and \
                        (self.__grid[row + 3][col] == player_on_white or self.__grid[row + 3][col] == player_on_black) and \
                        (self.__grid[row + 4][col] == player_on_white or self.__grid[row + 4][col] == player_on_black):
                    return True

        # check upward diagonal
        for row in range(3, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player_on_white and \
                        self.__grid[row - 1][col + 1] == player_on_white and \
                        self.__grid[row - 2][col + 2] == player_on_white and \
                        self.__grid[row - 3][col + 3] == player_on_white:
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player_on_white and \
                        self.__grid[row + 1][col + 1] == player_on_white and \
                        self.__grid[row + 2][col + 2] == player_on_white and \
                        self.__grid[row + 3][col + 3] == player_on_white:
                    return True

        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2
    
    def validate_add_action(self,action: DayAndNightAddAction) -> bool:
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
        if self.__grid[row][col] != BLK:
            return False

        return True

    def validate_move_action(self,action: DayAndNightMoveAction) -> bool:
        row_from = action.get_row_from()
        col_from = action.get_col_from()
        row_to = action.get_row_to()
        col_to = action.get_col_to()

        cell_from_value = self.__grid[row_from][col_from]
        
        # Get the last digit from the cell value
        player_index = int(str(cell_from_value)[len(str(cell_from_value)) - 1])
        
        # Check is cell from is empty
        if cell_from_value == WHI or cell_from_value == BLK:
            return False
        
        # Check if player as a piece on the from position
        if player_index != self.__acting_player:
            return False

        # valid column
        if col_to < 0 or col_to >= self.__num_cols:
            return False

        # valid row
        if row_to < 0 or row_to >= self.__num_rows:
            return False

        # valid move
        if self.__grid[row_to][col_to] != WHI or \
                abs(row_to - row_from) > 1 or abs(col_to - col_from) > 1:
            return False

        return True

    def validate_action(self, action: DayAndNightAction) -> bool:
        
        if isinstance(action,DayAndNightAddAction):
            return self.validate_add_action(action)
        if isinstance(action,DayAndNightMoveAction):
            return self.validate_move_action(action)

        return False

    def update(self, action: DayAndNightAction):
        
        if isinstance(action,DayAndNightAddAction):
            col = action.get_col()
            row = action.get_row()
            
            play = int(str(self.__grid[row][col]) + str(self.__acting_player))
    
            self.__grid[row][col] = play
          

        if isinstance(action,DayAndNightMoveAction):
            row_from = action.get_row_from()
            col_from = action.get_col_from()
            row_to = action.get_row_to()
            col_to = action.get_col_to()

            play = int(str(self.__grid[row_to][col_to]) + str(self.__acting_player))

            self.__grid[row_to][col_to] = play

            self.__grid[row_from][col_from] = int(str(self.__grid[row_from][col_from])[:-1])

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

    def __display_cell(self, row, col):
        print({
                  #0: ' B ',
                  #1: ' W ',
                  -10:'\033[1;40m B \033[0m',#◉
                  -11:'\033[1;40m W \033[0m',
                  -20:'\033[1;47m B \033[0m',
                  -21:'\033[1;47m W \033[0m',
                  BLK: '\033[1;40m   \033[0m',
                  WHI: '\033[1;47m   \033[0m'
              }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col==0:
                print(' ', end="")
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

    def display(self):
        print("  ", end="")
        self.__display_numbers()
        #self.__display_separator()

        for row in range(0, self.__num_rows):
            if row < 10:
                print(row,' |', end="")
            if row >= 10:
                print(row,'|', end="")
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
                if col == self.__num_cols-1:
                    print('|',row, end="")
                print('', end="")

            print("")
            
        print("  ", end="")
        #self.__display_separator()
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
    
    def get_possible_add_actions(self):
        return list(filter(
            lambda action: self.validate_add_action(action),
            [
                DayAndNightAddAction(row, col)
                for row in range(self.get_num_rows())
                for col in range(self.get_num_cols())
            ]
        ))
    
    def get_possible_move_actions(self):
        return list(filter(
            lambda action: self.validate_move_action(action),
            [
                DayAndNightMoveAction(row_from, col_from, row_to, col_to)
                for row_from in range(self.get_num_rows())
                for col_from in range(self.get_num_cols())
                for row_to in range(self.get_num_rows())
                for col_to in range(self.get_num_cols())
            ]
        ))

    def get_possible_actions(self):
        return list(filter(
            lambda action: self.validate_add_action(action),
            map(
                lambda pos: DayAndNightAction(pos),
                range(0, self.get_num_cols()))
        ))
    
    def get_possible_actions(self):
        return self.get_possible_add_actions() + self.get_possible_move_actions()

    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
