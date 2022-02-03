def circularArrayLoop(nums: list[int]) -> bool:
    dead_indexes = set()
    for i, move in enumerate(nums):
        current = i
        visited = set()
        while current not in visited:
            visited.add(current)
            current = (nums[current] + current) % len(nums)
            if current in dead_indexes:
                dead_indexes.update(visited)
                visited = set()
                break
        if not visited:
            continue
        not_in_cycle = set()
        stray_end = i
        while stray_end != current:
            not_in_cycle.add(stray_end)
            stray_end = (nums[stray_end] + stray_end) % len(nums)

        cycle = visited - not_in_cycle
        is_positive = all([nums[j] > 0 for j in cycle])
        is_negative = all([nums[j] < 0 for j in cycle])
        if len(cycle) > 1 and (is_positive or is_negative):
            return True
        else:
            dead_indexes.update(visited)
    return False