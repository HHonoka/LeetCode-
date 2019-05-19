class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, key: str, val: int) -> None:
        node = self.dic
        for c in key:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["#"] = val

    def sum(self, prefix: str) -> int:
        node = self.dic

        self.res = 0
        for c in prefix:
            if c not in node:
                return self.res
            node = node[c]
        def dfs(node):
            for n in node.keys():
                if n == "#":
                    self.res += node[n]
                else:
                    dfs(node[n])
        dfs(node)
        return self.res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)