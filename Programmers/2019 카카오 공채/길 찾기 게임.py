import heapq
def solution(nodeinfo):
    answer = [[]]
    new = []
    for idx,node in enumerate(nodeinfo):
        new.append([node[1],-node[0],idx+1])
    new.sort(reverse=True)
    print(new)
    return answer


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))