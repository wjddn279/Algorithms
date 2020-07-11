def permutation(n,k,r):
    if k == r:
        print(a)
        return
    else:
        for i in range(k,n+1):
            a[i],a[k] = a[k],a[i]
            permutation(n, k+1, r)
            a[i],a[k] = a[k],a[i]

def combination(n,r,k,result):
    if len(result) == r:
        print(result)
        return
    if k > n:
        return
    else:
        combination(n,r,k+1,result)
        combination(n,r,k+1,result+[a[k]])

def subset(n,k,result):
    if n == k:
        print(result)
    else:
        subset(n,k+1,result+[a[k]])
        subset(n,k+1,result)
a = [1,2,3,4]
# permutation(len(a)-1,0,2)
# combination(len(a)-1,2,0,[])
subset(len(a),0,[])