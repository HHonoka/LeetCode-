class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        self.dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.res = []
        self.dfs(digits, 0, "")
        return self.res

    def dfs(self, s, index, path):
        if len(path) == len(s):
            self.res.append(path)
            return
        for e in self.dic[s[index]]:
            self.dfs(s, index + 1, path + e)