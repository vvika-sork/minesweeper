from enum import Enum


class DifficultyLevel(Enum):
    """
        value: mines, rows, colums
    """
    EASY = 10, 9, 9
    MEDIUM = 40, 16, 16
    HARD = 90, 16, 30
