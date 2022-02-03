def fourSumCount(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    pairSums = {}
    for a in nums1:
        for b in nums2:
            pairSums[-(a+b)] = pairSums.get(-(a+b), 0) + 1
            
    total = 0
    for c in nums3:
        for d in nums4:
            if (c+d) in pairSums:
                total += pairSums[c+d]
                
    return total