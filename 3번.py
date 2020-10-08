from _collections import deque

def solution(n, edges):
    def chk(a):
        visited = [[-1,i] for i in range(n+1)]
        queue = deque()
        queue.append((a,0))
        visited[a][0] = 0
        while queue:
            now,cnt = queue.popleft()
            for can in tree[now]:
                if visited[can][0] == -1:
                    queue.append((can,cnt+1))
                    visited[can][0] = cnt+1
        return visited

    def dis(a,b):
        visited = [0 for i in range(n+1)]
        queue = deque()
        queue.append((a,0))
        visited[a] = 1
        while queue:
            now,cnt = queue.popleft()
            for can in tree[now]:
                if can == b:
                    return cnt+1
                if not visited[can]:
                    queue.append((can,cnt+1))
                    visited[can] = 1

    data = [[0,i] for i in range(n+1)]
    tree = [[] for _ in range(n+1)]
    for a,b in edges:
        tree[a].append(b)
        tree[b].append(a)
        data[a][0] += 1
        data[b][0] += 1
    data.sort()
    mem = chk(data[-1][1])
    mem.sort(reverse=True)
    route = [mem[i][1] for i in range(3)]
    arr = [dis(route[0],route[1]),dis(route[0],route[2]),dis(route[1],route[2])]
    arr.sort()
    return arr[1]

def a():
    k = [[0 for _ in range(25000)] for _ in range(25000)]
print(solution(4,[[1,2],[2,3],[3,4]]))