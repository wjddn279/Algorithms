def solution(p):
    global answer
    answer = ''
    recursive(p)
    return answer

def recursive(p):
    global answer
    if not p: return
    dic = {'(':')',')':'('}
    idx = isbalance(p)
    u,v = p[0:idx+1],p[idx+1:len(p)+1]
    if iscorrect(u):
        answer += u
        recursive(v)
    else:
        answer += '('
        recursive(v)
        answer += ')'
        answer += ''.join([dic[now] for now in u[1:len(u)-1]])

def iscorrect(s):
    stack = []
    for now in s:
        if stack and stack[-1] == '(' and now == ')':
            stack.pop()
        else:
            stack.append(now)
    if stack:
        return False
    else:
        return True

def isbalance(s):
    dic = {'(':0,')':0}
    for i in range(len(s)):
        dic[s[i]] += 1
        if dic['('] == dic[')']:
            return i

print(solution(")("))