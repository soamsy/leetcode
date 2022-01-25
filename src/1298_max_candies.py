import collections


def maxCandies(status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
    
    locked_boxes = set()
    unused_keys = set()
    q = collections.deque(initialBoxes)
    
    candy_bag = 0
    while q:
        box = q.popleft()
        if status[box] == 0 and box in unused_keys:
            status[box] = 1
            unused_keys.remove(box)
        
        if status[box]:
            candy_bag += candies[box]
            ks = keys[box]
            for k in ks:
                if k in locked_boxes:
                    q.append(k)
                    locked_boxes.remove(k)
                    status[k] = 1
                else:
                    unused_keys.add(k)
            new_boxes = containedBoxes[box]
            q.extend(new_boxes)
        else:
            locked_boxes.add(box)
            
    return candy_bag