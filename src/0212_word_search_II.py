import collections
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.isWord = False

    def insert(self, word):
        current = self
        for c in word:
            current = current.children[c]
        current.isWord = True

    def get(self, char):
        return self.children[char] if char in self.children else None
    
class Solution:    
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m, n = len(board), len(board[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        maxLength = max([len(word) for word in words])
        seq = []        
        answers = set()
        def backtrack(x, y, node):
            
            if board[x][y] == '#':
                return
            
            child = node.get(board[x][y])
            if child is None:
                return
            
            seq.append(board[x][y])
            if child.isWord:
                answers.add(''.join(seq))
                
            if len(seq) >= maxLength:
                seq.pop()
                return
            
            char = board[x][y]
            board[x][y] = '#'
            for d in dirs:
                xp, yp = x + d[0], y + d[1]
                if 0 <= xp < m and 0 <= yp < n:
                    backtrack(xp, yp, child)
            board[x][y] = char
            seq.pop()
        
        for x in range(m):
            for y in range(n):
                backtrack(x, y, trie)
                
        return list(answers)