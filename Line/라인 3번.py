def solution(n):

    answer = [float('inf'),float('inf')]
    def rec(a,b,k):
        if not b or not a:
            return
        if len(b) != 1 and b[0] == '0':
            return
        if len(a) != 1 and a[0] == '0':
            return
        now = str(int(a) + int(b))
        if len(now) == 1:
            if k < answer[0]:
                answer[0],answer[1] = k,int(now)
            return
        for i in range(len(now)):
            rec(now[0:i],now[i:len(now)],k+1)
    rec(str(n),'0',0)
    return answer

print(solution(73425))

