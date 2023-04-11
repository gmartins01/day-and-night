from games.day_and_night.action import DayAndNightAddAction
from games.day_and_night.action import DayAndNightMoveAction
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
                # aks if the player wants to add piece or move an existing piece
                action = input(f"Player {state.get_acting_player()}, choose an action ([1] add/[2] move): ")

                if action == "1" or action == "add":
                    return DayAndNightAddAction(int(input(f"Player {state.get_acting_player()}, choose a row: ")),
                                         int(input(f"Player {state.get_acting_player()}, choose a column: ")))

                elif action == "2" or action == "move":
                    return DayAndNightMoveAction(int(input(f"Player {state.get_acting_player()}, choose a row from: ")),
                                          int(input(f"Player {state.get_acting_player()}, choose a column from: ")),
                                          int(input(f"Player {state.get_acting_player()}, choose a row to: ")),
                                          int(input(f"Player {state.get_acting_player()}, choose a column to: ")))
                else:
                    print("Invalid action")
                    continue
                
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: DayAndNightState):
        # ignore
        pass

    def event_end_game(self, final_state: DayAndNightState):
        # ignore
        pass
