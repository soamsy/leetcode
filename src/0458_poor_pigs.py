import math
def poorPigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    rounds = minutesToTest // minutesToDie
    if rounds < 1:
        return 0
    
    pigs = 0
    while (rounds + 1) ** pigs < buckets:
        pigs += 1
    return pigs