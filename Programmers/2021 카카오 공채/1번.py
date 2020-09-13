def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    target = {'-':0,'_':0,'.':0}
    lv2 = ''
    for alpha in new_id:
        if alpha.isalpha() or alpha.isnumeric() or alpha in target:
            lv2 += alpha
    lv3 = ""
    for alpha in lv2:
        if lv3:
            if alpha == '.' and lv3[-1] == '.':
                continue
        lv3 += alpha
    lv4 = ""
    for idx,alpha in enumerate(lv3):
        if idx == 0 and alpha == '.':
            continue
        elif idx == len(lv3)-1 and alpha == '.':
            continue
        else:
            lv4 += alpha
    if not lv4:
        lv4 = "a"
    lv4 = lv4[0:15]
    total = len(lv4)
    if lv4[-1] == '.':
        lv4 = lv4[0:total-1]
    while len(lv4) <= 2:
        lv4 += lv4[-1]
    return lv4

print(solution(""))