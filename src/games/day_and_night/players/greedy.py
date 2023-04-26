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
    
    def get_distance(self, pos1, pos2):
        print("pos 1",pos1)
        print("pos 2",pos2)

        return abs(pos1[0] - pos2.get_row()) + abs(pos1[1] - pos2.get_col())

    def get_move_action(self, state: DayAndNightState):
        possible_move_actions = state.get_possible_move_actions()
        grid = state.get_grid()
        selected_move = None

        # get the black places where the player has pieces
        player_blk_pieces = []
        for row in range(0, state.get_num_rows()):
            for col in range(0, state.get_num_cols()):
                if grid[row][col] == int(str(state.EMPTY_BLK) + str(self.get_current_pos())):
                    player_blk_pieces.append((row, col))
        
        if len(player_blk_pieces) == 0:
            # player has no pieces on the board, can't move
            return None

        # choose the best move action
        for move_action in possible_move_actions:
            if selected_move is None:
                selected_move = move_action
            else:
                min_distance = float('inf')
                for blk_piece in player_blk_pieces:
                    distance = self.get_distance(blk_piece, move_action)
                    if distance < min_distance:
                        min_distance = distance
                if min_distance < self.get_distance(player_blk_pieces[0], selected_move):
                    selected_move = move_action

        return selected_move


    def get_add_action(self, state: DayAndNightState):
        possible_add_actions = state.get_possible_add_actions()
        grid = state.get_grid()
        selected_add = None
        num_rows = state.get_num_rows()
        num_cols = state.get_num_cols()

        # get the player pieces
        player_pieces = []
        for row in range(0, state.get_num_rows()):
            for col in range(0, state.get_num_cols()):
                if grid[row][col] == int(str(state.EMPTY_BLK) + str(self.get_current_pos())) or \
                    grid[row][col] == int(str(state.EMPTY_BLK) + str(self.get_current_pos())):
                    player_pieces.append((row, col))

        print("player_pieces",player_pieces)
        if len(player_pieces) == 0:
            # no pieces on the board, add a piece to the center
            return DayAndNightAddAction(choice([num_cols // 2, num_cols // 2 - 1]), 
                                       choice([num_rows // 2, num_rows // 2 - 1]))
        else:
            # choose the best add action
            min_distance = float('inf')
            for add_action in possible_add_actions:
                for player_piece in player_pieces:
                    distance = self.get_distance(player_piece, add_action)
                    if distance < min_distance:
                        min_distance = distance
                        selected_add = add_action

            return selected_add

    def get_action(self, state: DayAndNightState):
        grid = state.get_grid()
    
        move = self.get_move_action(state)
        if move is not None:
            return move
        
        add = self.get_add_action(state)
        if add is not None:
            return add
        
        # If there are no possible moves or add actions, return None
        return None

        


    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass