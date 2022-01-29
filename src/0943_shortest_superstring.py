import itertools
import functools
import math
def shortestSuperstring(words: list[str]) -> str:
    '''
    This is a travelling salesman problem, with the distances defined by how much more
    length you get by adding another word onto your current word. Once you have
    the distances nailed down, your options are either to:
    - compute the distance all permutations of words, which is O(n!), and works up to about n = 15
    - use dynamic programming, which creates a O(n^2 * 2^n) solution, and works up to about n = 23

    Since the leetcode test cases use n = 20, the following uses dynamic programming.
    '''

    def merge_len(a, b):
        for option in range(len(a)):
            if b.startswith(a[option:]):
                return len(b) - len(a[option:])

        return len(b)
    n = len(words)
    mat = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            if a != b:
                mat[a][b] = merge_len(words[a], words[b])
                mat[b][a] = merge_len(words[b], words[a])


    dp = [[0] * (1 << n) for _ in range(n)]
    path = [[0] * (1 << n) for _ in range(n)]

    for i in range(n):
        dp[i][1 << i] = len(words[i])

    total_bits = [1] * n
    for i in range(n):
        total_bits[i] = total_bits[i] << i

    def get_bits(combination):
        return functools.reduce(lambda a,b: a | b, combination)

    for to_take in range(2, n + 1):
        for comb in itertools.combinations(total_bits, to_take):
            visited_bits = get_bits(comb)
            for visiting_index in range(n):
                visiting_bit = 1 << visiting_index
                if visiting_bit & visited_bits == 0:
                    continue

                min_dist = float("infinity")
                others_bits = visited_bits & ~visiting_bit
                for last_visited_bit in comb:
                    if last_visited_bit == visiting_bit:
                        continue
                    last_visited_index = int(math.log(last_visited_bit, 2))
                    dist = dp[last_visited_index][others_bits] + mat[last_visited_index][visiting_index]
                    if dist < min_dist:
                        min_dist = dist
                        dp[visiting_index][visited_bits] = min_dist
                        path[visiting_index][visited_bits] = last_visited_index


    all_bits = get_bits(total_bits)
    min_path = 0
    shortest = float("infinity")
    for i in range(len(dp)):
        if dp[i][all_bits] < shortest:
            shortest = dp[i][all_bits]
            min_path = i

    order = []
    path_index, path_bits = min_path, all_bits
    for i in range(n):
        order.append(path_index)
        path_index = path[path_index][path_bits]
        path_bits = path_bits & ~(1 << order[-1])
        
    order = order[::-1]
    shortest_seq = words[order[0]]
    for i in range(1, n):
        word = words[order[i]]
        dist = mat[order[i-1]][order[i]]
        shortest_seq += word[len(word) - dist:]
        
    return shortest_seq