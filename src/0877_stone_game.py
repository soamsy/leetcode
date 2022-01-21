def stoneGame(piles: list[int]) -> bool:
    # If you split the piles up into 2 sets defined as:
    # 1st set: where you take pile 1, pile 3, pile 5, and so on
    # 2nd set: where you take pile 2, pile 4, pile 6, and so on
    # Alice can always force Bob to take all his piles from 1 of these sets,
    # meaning Alice will always win if she determines which set is higher
    # and forces Bob to take from the other one
    
    return True
    
    # Alternatively, you can simulate both players trying to take advantage of this mechanic
#         points = {
#             'alice': 0,
#             'bob': 0
#         }
    
#         turn = 'alice'
#         left = 0
#         right = len(piles) - 1
#         while left <= right:
#             right_potential = 0
#             for i in range(0, len(piles), 2):
#                 right_potential += piles[i]
#             left_potential = 0
#             for i in range(1, len(piles), 2):
#                 left_potential += piles[i]
            
#             if left_potential < right_potential:
#                 points[turn] += piles[left]
#                 left += 1
#             else:
#                 points[turn] += piles[right]
#                 right -= 1
            
#             turn = 'alice' if turn == 'bob' else 'bob'
        
#         return points['alice'] > points['bob']