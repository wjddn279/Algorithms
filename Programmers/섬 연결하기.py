import heapq

def solution(n, costs):
    answer = 0
    parents = [i for i in range(n+1)]

    def find(i):
        if parents[i] == i:
            return i
        parents[i] = find(parents[i])
        return parents[i]

    def union(a,b):
        pa,pb = find(a),find(b)
        if pa == pb:
            return True
        else:
            parents[pa] = pb
            return False
    costs.sort(key = lambda x:x[2])
    for a,b,c in costs:
        if not union(a,b):
            answer += c
    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))