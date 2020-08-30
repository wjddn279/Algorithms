from itertools import permutations

def solution(expression):
    answer = 0
    answer,bound,num = 0, {'*':0,'+':0,'-':0}, ''
    express = []
    for exp in expression:
        if exp in bound:
            express.append(num)
            express.append(exp)
            num = ''
        else:
            num += exp
    express.append(num)
    for operation in permutations(['+','*','-'],3):
        exp = express[:]
        temp = []
        idx = 0
        for oper in operation:
            while idx < len(exp):
                if exp[idx] == oper:
                    temp[-1] = str(operate(temp[-1],exp[idx+1],exp[idx]))
                    idx += 2
                else:
                    temp.append(exp[idx])
                    idx += 1
            exp = temp[:]
            temp = []
            idx = 0
        answer = max(answer,abs(int(exp[0])))
    return answer

def operate(a,b,o):
    if o == '+': return int(a)+int(b)
    if o == '*': return int(a)*int(b)
    if o == '-': return int(a)-int(b)

print(solution("100-200*300-500+20"))