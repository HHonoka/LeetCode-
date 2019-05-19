class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = collections.defaultdict(dict)
        for i in range(len(equations)):
            dic[equations[i][0]][equations[i][1]] = values[i]
            dic[equations[i][1]][equations[i][0]] = 1 / values[i]
        print(dic)
        def search(i, j, seen):
            if i == j:
                return 1.0
            seen.add(i)
            for node in dic[i]:
                if node in seen:
                    continue
                seen.add(node)
                num = search(node, j, seen)
                if num > 0:
                    return num * dic[i][node]
            return -1.0
        res = []
        for i in range(len(queries)):
            if queries[i][0] in dic and queries[i][1] in dic:
                res.append(search(queries[i][0], queries[i][1], set()))
            else:
                res.append(-1.0)
        return res