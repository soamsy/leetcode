def findMedianSortedArrays(nums1, nums2):
    if (len(nums1) > len(nums2)):
        nums1, nums2 = nums2, nums1
    
    total_size = len(nums1) + len(nums2)
    median_loc = (total_size) // 2
    
    def binary(l, r):
        lm = (l + r) // 2
        rm = median_loc - lm - 2

        lleft = nums1[lm] if lm >= 0 else float("-infinity")
        lright = nums1[lm + 1] if (lm + 1) < len(nums1) else float("infinity")
        rleft = nums2[rm] if rm >= 0 else float("-infinity")
        rright = nums2[rm + 1] if (rm + 1) < len(nums2) else float("infinity")

        if lleft <= rright and rleft <= lright:
            rside = min(lright, rright)
            lside = max(lleft, rleft)
            if total_size % 2 == 1:
                return rside
            else:
                return (rside + lside) / 2
        elif lleft > rright:
            return binary(l, lm - 1)
        else:
            return binary(lm + 1, r)

    return binary(0, len(nums1) - 1)



"""
print(findMedianSortedArrays([], [1]))
print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 2, 3, 8], [5, 6]))
"""