def generateParenthesis(n: int) -> list[str]:
    def recur(s, open, closed):
        choices = []
        if open < n:
            choices.extend(recur(s + "(", open + 1, closed))
        if closed < open <= n:
            choices.extend(recur(s + ")", open, closed + 1))
        if open >= closed >= n:
            choices.append(s)
        
        return choices
    return recur("", 0, 0)