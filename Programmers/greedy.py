def solution(n, lost, reserve):
    answer = 0
    data = [1 for _ in range(n+2)]
    for num in lost:
        data[num] -= 1
    for num in reserve:
        data[num] += 1
    for idx in range(1,len(data)):
        if data[idx] == 2:
            data[idx] -= 1
            if data[idx-1] == 0:
                data[idx-1] += 1
            elif data[idx+1] == 0:
                data[idx+1] += 1
    for idx in range(1,n+1):
        if data[idx] > 0:
            answer += 1
    return answer

def solution(number, k):
    answer = ''
    data = list(map(int,number))
    print(data)
    return answer

def solution(name):
    answer1,answer2,answer3 = 0,0,0
    total = len(name)-1
    alpha = {
        'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
        'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,
        'V':21,'W':22,'X':23,'Y':24,'Z':25
    }
    temp = 0
    for idx in range(len(name)):
        number = alpha[name[idx]]
        answer1 += min(number,26-number)
        temp += 1
        if idx < total and name[idx+1] != 'A':
            answer1 += temp
            temp = 0
    seq = [0]+list(range(len(name)-1,0,-1))
    temp = 0
    for idx in range(len(name)):
        number = alpha[name[seq[idx]]]
        answer2 += min(number,26-number)
        temp += 1
        if idx < total and name[seq[idx+1]] != 'A':
            answer2 += temp
            temp = 0
    result = float('inf')
    for n in range(len(name)):
        answer3 = 0
        seq = list(range(0,n+1))
        temp = 0
        for idx in range(len(seq)):
            number = alpha[name[idx]]
            answer3 += min(number,26-number)
            temp += 1
            if idx < len(seq)-1 and name[idx+1] != 'A':
                answer3 += temp
                temp = 0
        answer3 += n
        seq = [0]+list(range(len(name)-1,n,-1))
        temp = 0
        for idx in range(len(seq)):
            print(name[seq[idx]])
            number = alpha[name[seq[idx]]]
            answer3 += min(number,26-number)
            temp += 1
            if idx < len(seq)-1 and name[seq[idx+1]] != 'A':
                answer3 += temp
                temp = 0
        result = min(result,answer3)
    return min(answer1,answer2,result)

print(solution("ABAAAAABB"))