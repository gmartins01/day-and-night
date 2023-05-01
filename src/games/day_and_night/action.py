from abc import ABC

class DayAndNightAction(ABC):
    def init(self):
        self

class DayAndNightPlayAction(DayAndNightAction,ABC):
    def init(self):
        self

class DayAndNightMoveAction(DayAndNightPlayAction):
    row_from: int
    col_from: int
    row_to: int
    col_to: int

    def __init__(self,row_from: int, col_from: int, row_to: int, col_to: int):
        self.row_from = row_from
        self.col_from = col_from
        self.row_to = row_to
        self.col_to = col_to

    def get_row_from(self):
        return self.row_from
    
    def get_col_from(self):
        return self.col_from
    
    def get_row_to(self):
        return self.row_to
    
    def get_col_to(self):
        return self.col_to
    
class DayAndNightAddAction(DayAndNightPlayAction):
    row: int
    col: int

    def __init__(self,row: int, col: int):
        self.row = row
        self.col = col

    def get_row(self):
        return self.row
    
    def get_col(self):
        return self.col

    