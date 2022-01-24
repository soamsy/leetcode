def findNumbers(self, nums: list[int]) -> int:
    lengths = [len(str(x)) % 2 == 0 for x in nums]
    return len([l for l in lengths if l])