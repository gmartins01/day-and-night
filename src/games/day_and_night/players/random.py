from random import randint
import random
from games.day_and_night.player import DayAndNightPlayer
from games.day_and_night.state import DayAndNightState
from games.state import State


class RandomDayAndNightPlayer(DayAndNightPlayer):

    def __init__(self, name):
        super().__init__(name)
        self.add_turn_counter = 0
        self.move_turn_counter = 0
        
    def get_action(self, state: DayAndNightState):
        grid = state.get_grid()
        #state.display()
        possible_add_actions = state.get_possible_add_actions()
        possible_move_actions = state.get_possible_move_actions()
        if self.add_turn_counter < 4 and len(possible_add_actions) > 0:
            action = random.choice(possible_add_actions) 
            self.add_turn_counter += 1
            return action
        
        elif self.move_turn_counter < 2 and len(possible_move_actions) > 0:
            action = random.choice(possible_move_actions)
            self.move_turn_counter += 1
            return action
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
