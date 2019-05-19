class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False]*len(rooms)
        stack = [0]
        seen[0] = True
        while stack:
            node = stack.pop()
            for n in rooms[node]:
                if seen[n] == False:
                    stack.append(n)
                    seen[n] = True
        return False not in seen