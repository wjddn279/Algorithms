import sys
sys.stdin = open("a.txt")
def battle(x,y):
    if x == y:
        return x,0
    elif x == 1 and y == 3:
        return x,0
    elif x == 2 and y == 1:
        return x,0
    elif x == 3 and y == 2:
        return x,0
    else:
        return y,1
def recursive(data,seq):
    L = len(data)-1
    if len(data) == 1:
        result.append(data[0])
        seq_result.append(seq[0])
        return
    if len(data) == 2:
        a,b = battle(data[0],data[1])
        result.append(a)
        seq_result.append(seq[b])
        return
    else:
        recursive(data[0:(L//2)+1],seq[0:(L//2)+1])
        recursive(data[(L//2)+1:L+1],seq[(L//2)+1:L+1])
T = int(input())
for test_case in range(1,T+1):
    length = int(input())
    data = list(map(int,input().split()))
    seq = list(range(1,length+1))
    result = []
    while len(result) != 1:
        seq_result = []
        result = []
        recursive(data,seq)
        data = []
        for i in result:
            data.append(i)
        seq = []
        for i in seq_result:
            seq.append(i)

    print("#{} {}".format(test_case,*seq_result))

age = 3
sentence = f'김민지의 나이는 {age}'
