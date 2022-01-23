def sequentialDigits(self, low: int, high: int) -> list[int]:
    low_power = len(str(low))
    high_power = len(str(high))
    candidates = []

    for power in range(low_power, high_power + 1):
        for i in range(1,11-power):
            candidate = ""
            for j in range(i, i + power):
                candidate += str(j)
            candidates.append(int(candidate))
    
    return [c for c in candidates if low <= c <= high]