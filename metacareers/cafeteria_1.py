from typing import List
import math 
# Write any import statements here
 
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
 # Write your code here
  seats_list = N * [0]
  for seat in S:
    # Mark seats to the left and right of the diner as blocked
    seats_blocked_right = min(seat + K, N)
    seats_blocked_left = max(seat - K, 1)
    
    for i in range (seats_blocked_left-1, seats_blocked_right):
      seats_list[i] = 1
    
  aux_seat_list = []
  new_dinners = 0 
  
  for i, seat in enumerate(seats_list):
    if seat == 0:
      aux_seat_list.append(0)
      #print(aux_seat_list)
    elif len(aux_seat_list) > 0:
      new_dinners += maxDinnersCount(len(aux_seat_list), K)
      #print(new_dinners)
      aux_seat_list = []
    if i >= len(seats_list)-1:
      #print(maxDinnersCount(len(aux_seat_list), K))
      new_dinners += maxDinnersCount(len(aux_seat_list), K)
      #print(new_dinners)
      
    
  return new_dinners

def maxDinnersCount(N: int,  K: int) -> int :
  return math.ceil(N/(K + 1))
