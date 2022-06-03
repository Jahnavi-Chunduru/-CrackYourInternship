from collections import defaultdict,deque
class Solution:
    def removeStones(self, stones):
        stone_id = set()
        x_map = defaultdict(list)
        y_map = defaultdict(list)
        stone_map = {}
        for i, (x,y) in enumerate(stones):
            stone_map[i] = (x,y)
            x_map[x].append(i)
            y_map[y].append(i)
            stone_id.add(i)
        ans = 0

        while len(stone_id) > 0:
            stack = deque()
            stack.append(stone_id.pop())
            nums = 0
            while len(stack) > 0:
                idx = stack.popleft()
                nums += 1
                x,y = stone_map[idx]
                for i in x_map[x]:
                    if i in stone_id:
                        stack.append(i)
                        stone_id.remove(i)
                for i in y_map[y]:
                    if i in stone_id:
                        stack.append(i)
                        stone_id.remove(i)
            ans += nums-1
        return ans
