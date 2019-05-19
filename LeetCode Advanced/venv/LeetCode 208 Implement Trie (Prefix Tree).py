class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.dic
        for w in word:
            if w in node:
                node = node[w]
            else:
                node[w] = {}
                node = node[w]
        node['end'] = None
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.dic
        for w in word:
            if w not in node:
                return False
            node = node[w]
        return True if 'end' in node else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.dic
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)