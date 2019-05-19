class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dp = [float('inf') for _ in range(N + 1)]
        dp[K] = 0
        dp[0] = 0
        for _ in range(N - 1):
            for x, y, z in times:
                if dp[x] + z < dp[y]:
                    dp[y] = dp[x] + z
        return -1 if max(dp) >= float('inf') else max(dp)
#Bellman-Ford

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dic = collections.defaultdict(dict)
        for u, v, w in times:
            dic[u][v] = w
        dist = {}
        stack = [(0, K)]
        while stack:
            p, node = heapq.heappop(stack)
            if node in dist:
                continue
            dist[node] = p
            for n in dic[node]:
                if n not in dist:
                    heapq.heappush(stack, (p + dic[node][n], n))
        return max(dist.values()) if len(dist) == N else -1
#Heap + Dijkstra
#We can get the time to each node from heap sort()
#The maximum value is the answer.
#Because it is means this is the last node we reached.