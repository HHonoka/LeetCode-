class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        self.dic = {}
        for word in dict:
            node = self.dic
            for w in word:
                if w not in node:
                    node[w] = {}
                    node = node[w]
                else:
                    node = node[w]
            node['end'] = None
        s = sentence.split()
        for i in range(len(s)):
            path = ''
            node = self.dic
            for c in s[i]:
                if c not in node:
                    if 'end' not in node:
                        break
                    else:
                        s[i] = path
                        break
                else:
                    if 'end' in node:
                        s[i] = path
                        break
                    else:
                        path += c
                        node = node[c]
        return ' '.join(s)

#In python, we can use startwith(), but this method is too slow when the data is very large.