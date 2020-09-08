import sys
sys.stdin = open("../input.txt")

def operation(a,o,b):
    if o == '+':
        return int(a)+int(b)
    if o == '-':
        return int(a) - int(b)
    if o == '*':
        return int(a) * int(b)

def powerser(n,k,step):
    if n == k:
        new,last,cnt = [], 0,0
        for i in range(len(data)):
            if i%2 == 0 and step[i//2] == 1:
                if last == '(':
                    return
                new.append('(')
                new.append(data[i])
                last = '('
                cnt += 1
            elif i%2 == 0 and step[i//2] == 2:
                if last == ')':
                    return
                new.append(data[i])
                new.append(')')
                last = ')'
                cnt += 1
            else:
                new.append(data[i])
        if last == '(' or cnt%2:
            return
        stack, oper = [], []
        for idx,con in enumerate(new):
            if con not in op:
                stack.append(con)
            else:
                if con == ')':
                    if idx - cnt > 4:
                        return
                    while oper[-1] != '(':
                        stack.append(oper.pop())
                    oper.pop()
                elif con == '(':
                    oper.append('(')
                    cnt = idx
                else:
                    if oper:
                        if oper[-1] == '+' or oper[-1] == '-' or oper[-1] == '*':
                            stack.append(oper.pop())
                    oper.append(con)
        stack += oper
        num= []
        for i in stack:
            if i not in op:
                num.append(i)
            else:
                a = num.pop()
                b = num.pop()
                temp = operation(b,i,a)
                num.append(temp)
        max_val[0] = max(max_val[0],num[0])
    else:
        powerser(n,k+1,step+[0])
        powerser(n,k+1,step+[1])
        powerser(n,k+1,step+[2])

N = int(input())
data = list(input())
op = {'+':0,'-':0,'*':0,'(':0,')':0}
max_val = [-float('inf')]
if N == 1:
    print(data[0])
else:
    powerser(N//2+1,0,[])
    print(max_val[0])
