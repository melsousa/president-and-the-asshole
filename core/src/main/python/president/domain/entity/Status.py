from enum import Enum


class Status(Enum):
    WAITING = "WAITING"
    IN_SORTING = "SORTING"
    IN_GAME = "IN_GAME"
    ROUND = "ROUND"
    ROUND_FINISHED = "ROUND_FINISHED"
    FINISHED = "FINISHED"
