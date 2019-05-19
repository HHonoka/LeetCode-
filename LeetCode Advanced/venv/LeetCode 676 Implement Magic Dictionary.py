class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            node = self.dic
            for c in word:
                if c in node:
                    node = node[c]
                else:
                    node[c] = {}
                    node = node[c]
            node['end'] = None
        print(self.dic)
    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        def helper(count, word, dic):
            if count > 1:
                return False
            if not word:
                if dic and 'end' in dic and count == 1:
                    return True
                return False
            if not dic:
                return False
            for k in dic:
                if k == word[0]:
                    if helper(count, word[1:], dic[k]):
                        return True
                else:
                    if helper(count + 1, word[1:], dic[k]):
                        return True
            return False
        return helper(0, word, self.dic)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)