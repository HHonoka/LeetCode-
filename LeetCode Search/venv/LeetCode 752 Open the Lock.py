class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        deadends = set(deadends)
        if start in deadends:
            return -1
        queue = collections.deque([(start, 0)])
        seen = set(start)
        while queue:
            node, step = queue.popleft()
            for i in range(0, 4):
                for j in [-1, 1]:
                    if int(node[i]) == 0 and j == -1:
                        newnode = node[:i] + "9" + node[i + 1:]
                    elif int(node[i]) == 9 and j == 1:
                        newnode = node[:i] + "0" + node[i + 1:]
                    else:
                        newnode = node[:i] + str(int(node[i]) + j) + node[i + 1:]
                    if newnode == target:
                        return step + 1
                    if newnode not in seen and newnode not in deadends:
                        queue.append((newnode, step + 1))
                        deadends.add(newnode)
        return -1
#BFS
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = int("0000")
        target = int(target)
        deadends = set(int(x) for x in deadends)
        if start in deadends:
            return -1
        queue = collections.deque([(start, 0)])
        seen = set([start])
        bases = [1, 10, 100, 1000]
        while queue:
            node, step = queue.popleft()
            for i in range(0, 4):
                r = (node // bases[i]) % 10
                for j in [-1, 1]:
                    newnode = node + ((r + j + 10) % 10 - r) * bases[i]
                    if newnode == target:
                        return step + 1
                    if newnode not in seen and newnode not in deadends:
                        queue.append((newnode, step + 1))
                        deadends.add(newnode)
        return -1

#BFS + int state
#From HuaHua