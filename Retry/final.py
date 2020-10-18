a = [1,2,3,4,5,6]
answer = []

def combination(n,k,r,step):
    if len(step) == r:
        answer.append(step)
        return
    if k == n:
        return
    combination(n,k+1,r,step+[a[k]])
    combination(n,k+1,r,step)

flag = [0 for _ in range(len(a))]

def permutation(n,r,step):
    if len(step) == r:
        answer.append(step)
        return
    for i in range(n):
        if not flag[i]:
            flag[i] = True
            permutation(n,r,step+[a[i]])
            flag[i] = False

permutation(len(a)-1,2,[])
print(len(answer))
print(len(list(set(answer))))