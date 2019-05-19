class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = collections.deque([(beginWord, 1)])
        wordList = set(wordList)
        seen = set()
        ls = string.ascii_lowercase
        while queue:
            word, count = queue.popleft()
            if word == endWord:
                return count
            for i in range(len(word)):
                for l in ls:
                    if l != word[i]:
                        newword = word[:i] + l + word[i + 1:]
                        if newword not in seen and newword in wordList:
                            queue.append((newword, count + 1))
                            seen.add(newword)
        return 0
#BFS

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s1 = {beginWord}
        s2 = {endWord}
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        wordList.remove(endWord)
        step = 0
        ls = string.ascii_lowercase
        while len(s1) > 0 and len(s2) > 0:
            step += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            s = set()
            newwords = set()
            for word in s1:
                for i in range(len(word)):
                    for l in ls:
                        if l != word[i]:
                            newword = word[:i] + l + word[i + 1:]
                            newwords.add(newword)
            for nword in newwords:
                if nword in s2:
                    return step + 1
                if nword not in wordList:
                    continue
                wordList.remove(nword)
                s.add(nword)
            s1 = s
        return 0
#Bidirectional BFS