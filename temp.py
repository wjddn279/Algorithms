import sys
sys.stdin = open("input.txt")

from itertools import combinations

from itertools import combinations

T = int(input())
for test_case in range(1, 1 + T):
    D, W, K = map(int, input().split())
    DATA = [list(map(int, input().split())) for _ in range(D)]
    result = K
    for cnt in range(K):  # 0 ~ K - 1
        for AB in ([0] * cnt, [1] * cnt):
            for idx in combinations(range(D), cnt):
                for line in zip(*DATA):
                    line = list(line)
                    # 약물 주입
                    for i in range(cnt):
                        line[idx[i]] = AB[i]
                    # 결과 확인
                    for y in range(D - K + 1):
                        temp = line[y]
                        for dy in range(1, K):
                            if temp != line[y + dy]:
                                break  # 조건 미충족, 다음 y 확인
                        else:
                            # 조건 충족, 다음 x 확인
                            break
                    else:
                        # 한 줄 전체가 조건 미충족. 다른 경우의 수 확인
                        break
                else:
                    # 모두 조건 충족. 결과 갱신
                    result = cnt
                    break
            else:
                continue
            break
        else:
            continue
        break
    print('#{} {}'.format(test_case, result))