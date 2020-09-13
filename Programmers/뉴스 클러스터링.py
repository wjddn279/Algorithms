def str_to_sub(str1):
    sub1 = []
    for con in range(len(str1)-1):
        if str1[con].isalpha() and str1[con+1].isalpha():
            sub1.append(str1[con].lower()+str1[con+1].lower())
    return sub1

def subset(sub1,sub2):
    cnt = 0
    for alp in sub1:
        if alp in sub2:
            cnt += 1
            sub2.remove(alp)
    return cnt

def solution(str1, str2):
    sub1,sub2 = str_to_sub(str1),str_to_sub(str2)
    len1,len2 = len(sub1),len(sub2)
    if len1 < len2:
        cnt = subset(sub2,sub1)
    else:
        cnt = subset(sub1,sub2)
    if len1+len2-cnt == 0:
        return 65536
    else:
        return int(cnt/(len1+len2-cnt) * 65536)


print(solution("aa1+aa2","AAAA12"))
