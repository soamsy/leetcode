import collections
class WordDictionary:

    def __init__(self):
        self.children = collections.defaultdict(WordDictionary)
        self.isWord = False
        

    def addWord(self, word: str) -> None:
        current = self
        for c in word:
            current = current.children[c]
        current.isWord = True
    
    def printTree(self, node):
        print(' '.join([c for c in node.children.keys()]))
        for n in node.children.values():
            self.printTree(n)
        
    def search(self, word: str) -> bool:
        def fn(node, i):
            if i >= len(word):
                return node.isWord
            if word[i] == '.':
                for child in node.children.values():
                    if fn(child, i+1):
                        return True
                return False
            return word[i] in node.children and fn(node.children[word[i]], i+1)
        return fn(self, 0)