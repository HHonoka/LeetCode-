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
        print(self.dic)
    def sum(self, prefix: str) -> int:
        node = self.dic
        print(node)
        self.res = 0
        for c in prefix:
            if c not in node:
                return self.res
            node = node[c]
        def dfs(node):
            for n in node.keys():
                print(n)
                if n == "#":
                    self.res += node[n]
                else:
                    dfs(node[n])
                    print(node[n])
        dfs(node)
        return self.res

obj = MapSum()
obj.insert("Apple",3)
param_2 = obj.sum("App")
print(param_2)