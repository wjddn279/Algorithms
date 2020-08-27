# 타겟 넘버
def solution(num, tar):
    global answer,numbers,target
    numbers,target,answer = num,tar,0
    solve(len(numbers),0,0)
    return answer

def solve(n,k,now):
    global answer,numbers,target
    if n == k and now == target:
        answer += 1
    elif n != k:
        solve(n,k+1,now+numbers[k])
        solve(n,k+1,now-numbers[k])

# 네트워크
# 2시부터 시작 -> 10분컷
from _collections import deque

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            answer += 1
            queue = deque()
            queue.append(i)
            visited[i] = 1
            while queue:
                k = queue.popleft()
                for j in range(n):
                    if not visited[j] and computers[k][j] == 1:
                        queue.append(j)
                        visited[j] = 1
    return answer

# 단어 변환
from _collections import deque

def solution(begin, target, words):
    queue = deque()
    for word in words:
        if isword(begin,word):
            if word == target:
                return 1
            else:
                queue.append((word,[word]))
    while queue:
        print(queue)
        now , step = queue.popleft()
        for word in words:
            if word not in step and isword(now,word):
                if word == target:
                    return len(step)+1
                else:
                    queue.append((word,step+[word]))
    return 0

def isword(now,word):
    cnt = 0
    for idx,alpha in enumerate(word):
        if alpha != now[idx]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

# 여행 경로

from _collections import deque

def solution(tickets):
    answer = []
    queue = deque()
    visited = [0 for _ in range(len(tickets))]
    for idx,ticket in enumerate(tickets):
        if ticket[0] == 'ICN':
            if not len(queue):
                queue.append([idx,[idx]])
            elif alpha(ticket[1],tickets[queue[-1][0]][1]):
                queue[0] = [idx,[idx]]
    visited[queue[0][0]] = 1
    while queue:
        now, step = queue.popleft()
        for idx,ticket in enumerate(tickets):
            if ticket[0] == tickets[now][1] and not visited[idx]:
                if not len(queue):
                    queue.append([idx, step+[idx]])
                elif alpha(ticket[1], tickets[queue[-1][0]][1]):
                    queue[0] = [idx, step+[idx]]
        if len(queue):
            visited[queue[0][0]] = 1
    answer = tickets[step[0]]
    for i in range(1,len(step)):
        answer += [tickets[step[i]][1]]
    return answer

def solution(tickets):
    answer = []
    queue = deque()
    for idx,ticket in enumerate(tickets):
        if ticket[0] == 'ICN':
            queue.append([idx,[idx],[ticket[0],ticket[1]]])
    while queue:
        now, step, air = queue.popleft()
        for idx,ticket in enumerate(tickets):
            if ticket[0] == tickets[now][1] and idx not in step:
                if len(step) == len(tickets) - 1:
                    answer.append(air+[ticket[1]])
                else:
                    queue.append([idx, step+[idx], air+[ticket[1]]])
    answer.sort()
    return answer[0]

def alpha(a,b):
    # a가 우선이면 true b가 우선이면 false
    data = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,
            'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,
            'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,
            'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,
            'Y':24,'Z':25,}
    for i in range(3):
        if data[a[i]] < data[b[i]]:
            return True
        elif data[a[i]] > data[b[i]]:
            return False

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))