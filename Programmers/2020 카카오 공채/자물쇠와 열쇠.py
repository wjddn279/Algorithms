def solution(key, lock):
    def search(i,j,length):
        cnt = 0
        for x in range(i,i+length):
            for y in range(j,j+length):
                if lock[x][y] == 0:
                    cnt += 1
        if cnt == lock_total:
            return True
        else:
            return False
    def lock_splitting():
        for length in range(1, lock_length + 1):
            for i in range(0, lock_length - length + 1):
                for j in range(0, lock_length - length + 1):
                    if search(i, j, length):
                        sub_lock = []
                        for x in range(i, i + length):
                            temp = []
                            for y in range(j, j + length):
                                temp.append(lock[x][y])
                            sub_lock.append(temp)
                        return sub_lock
    def solve():
        if check(0,len(sub_lock),0,len(sub_lock)):
            return True
        if check(0,len(sub_lock),len(key)-len(sub_lock),len(key)):
            return True
        if check(len(key)-len(sub_lock),len(key),0,len(sub_lock)):
            return True
        if check(len(key)-len(sub_lock),len(key),len(key)-len(sub_lock),len(key)):
            return True
        return False

    def rotate():
        new_matrix = [[0] * len(key) for i in range(len(key))]
        for i in range(len(key)):
            for j in range(len(key)):
                new_matrix[j][len(key) - i - 1] = key[i][j]
        return new_matrix

    def rotate_reverse():
        new_matrix = [[0] * len(key) for i in range(len(key))]
        for i in range(len(key)):
            for j in range(len(key)):
                new_matrix[len(key)- j - 1][i] = key[i][j]
        return new_matrix

    def check(a,b,c,d):
        for x,i in enumerate(list(range(a,b))):
            for y,j in enumerate(list(range(c,d))):
                if key[i][j] == sub_lock[x][y]:
                    return False
        return True

    answer = False
    lock_length = len(lock)
    lock_total = 0
    for i in range(lock_length):
        for j in range(lock_length):
            if lock[i][j] == 0:
                lock_total += 1
    sub_lock = lock_splitting()
    for i in range(4):
        key = rotate()
        answer = solve()
        if answer:
            return answer
    for i in range(4):
        key = rotate_reverse()
        answer = solve()
        if answer:
            return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))