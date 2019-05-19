class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordList = set(wordList)
        res = []
        dic = collections.defaultdict(list)
        dic[beginWord] = [[beginWord]]
        ls = string.ascii_lowercase
        while dic:
            newdic = collections.defaultdict(list)
            for word in dic:
                if word == endWord:
                    res.extend(path for path in dic[word])
                else:
                    for i in range(len(word)):
                        for l in ls:
                            if l != word[i]:
                                newword = word[:i] + l + word[i + 1:]
                                if newword in wordList:
                                    newdic[newword] += [path + [newword] for path in dic[word]]
            wordList -= set(newdic.keys())
            dic = newdic
        return res

