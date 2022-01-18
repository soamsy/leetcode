def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    count = 0
    for i in range(len(flowerbed)):
        leftfree = i == 0 or flowerbed[i - 1] == 0
        centerfree = flowerbed[i] == 0
        rightfree = i == (len(flowerbed) - 1) or flowerbed[i + 1] == 0
        if leftfree and centerfree and rightfree:
            count += 1
            flowerbed[i] = 1
    if count >= n:
        return True
    return False