from typing import List
import math 

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S.sort()
    extra_space = 0
    first_open_seat = 1
    
    for taken_seat in S:
        open_seats = taken_seat - K - first_open_seat
        if open_seats > 0:
            extra_space += (open_seats + K) // (K + 1)
        first_open_seat = taken_seat + K + 1
    
    open_seats = N + 1 - first_open_seat
    if open_seats > 0:
        extra_space += (open_seats + K) // (K + 1)
        
    return extra_space