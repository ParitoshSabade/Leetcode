class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        colMap = defaultdict(list)
        rowMap = defaultdict(list)

        for x,y in stones:
            rowMap[x].append((x,y))
            colMap[y].append((x,y))

        q = deque()
        visited = set()
        count = 0
        for st in stones:
            if (st[0],st[1]) not in visited:
                q.append((st[0],st[1]))
                while q:
                    stone = q.popleft()
                    print(f"stone: {stone}")
                    visited.add(stone)
                    for s in rowMap[stone[0]]:
                        if s not in visited:
                            q.append(s)
                    for s in colMap[stone[1]]:
                        if s not in visited:
                            q.append(s)
                count+=1
        return len(stones)-count



        
        return 0
