def maximumWealth(accounts: list[list[int]]) -> int:
    return sum(max(accounts, key=sum))