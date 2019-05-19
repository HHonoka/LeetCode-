class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dp = [float('inf') for _ in range(n)]
        dp[src] = 0
        print(dp)
        for _ in range(K + 1):
            temp = list(dp)
            for f in flights:
                temp[f[1]] = min(temp[f[1]], dp[f[0]] + f[2])
            dp = temp
        return -1 if dp[dst] >= float('inf') else dp[dst]


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dic = collections.defaultdict(dict)
        stack = [(0, src, K + 1)]
        for f in flights:
            dic[f[0]][f[1]] = f[2]
        while stack:
            p, node, k = heapq.heappop(stack)
            if node == dst:
                return p
            if k > 0:
                for n in dic[node]:
                    heapq.heappush(stack, (p + dic[node][n], n, k - 1))
        return -1
# Dijkstra's algorithm