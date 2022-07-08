class TrieNode:
    def __init__(self):
        self.children = {} # a : TrieNode
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        
        def find(temp: TrieNode, index: int) -> bool:
            cur = temp
            while index < len(word):
                if word[index] == ".":
                    for child in cur.children.values():
                        if find(child, index+1):
                            return True
                    return False
                    
                else:
                    if word[index] not in cur.children:
                        return False
                    cur = cur.children[word[index]]
                    index += 1
            return cur.isEndOfWord
        
        return find(self.root, 0)
                            
