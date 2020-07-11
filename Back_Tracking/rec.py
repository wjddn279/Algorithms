def sort_for(a):
    for i in range(len(a)):
        min = i
        for j in range(i,len(a)):
            if a[min]>a[j]:
                min = j
        a[min],a[i] = a[i],a[min]
    return a


def sort_rec(a,s):
    if s == len(a)-1:
        return a
    min = s
    for j in range(s,len(a)):
        if a[min] > a[j]:
            min = j
    a[min],a[s] = a[s],a[min]
    sort_rec(a,s+1)

def Permutation(a,s):
    if s == len(a):
        print(a)
        return
    for i in range(s,len(a)):
        a[i],a[s] = a[s],a[i]
        Permutation(a,s+1)
        a[i],a[s] = a[s],a[i]

a = [1,3,2]

print(sort_for(a))
sort_rec(a,0)
print(a)
Permutation(a,0)