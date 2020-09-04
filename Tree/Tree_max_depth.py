Tree = [3,9,20,None,None,15,7]

from _collections import deque

def bfs(Tree):
    queue = deque([0])
    total = len(Tree)
    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)):
            now = queue.popleft()
            left,right = 2 * now + 1, 2 * now + 2
            if left < total and Tree[left]:
                queue.append(left)
            if right < total and Tree[right]:
                queue.append(right)
    return depth


print(bfs(Tree))