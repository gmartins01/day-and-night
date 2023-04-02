class DayAndNightAction:
    """
    a day and night action only takes the value of the column and row to play
    """
    __col: int
    __row: int

    def __init__(self,row: int, col: int):
        self.__row = row
        self.__col = col

    def get_row(self):
        return self.__row
    
    def get_col(self):
        return self.__col
    
    
    