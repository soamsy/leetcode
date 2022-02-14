import collections
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.isWord = False
        
    def insert(self, word: str) -> None:
        current = self
        for c in word:
            current = current.children[c]
        current.isWord = True
            
    def search(self, word: str) -> bool:
        current = self
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        current = self
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True