from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        groups[str(sorted(s))].append(s)
    
    return groups.values()