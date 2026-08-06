class TrieNode:
    def __init__(self, val):
        self.val = val
        self.endOfWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.node = TrieNode('')

    def addWord(self, word: str) -> None:
        curr = self.node

        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            curr = node
            
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.endOfWord
        return dfs(0, self.node)