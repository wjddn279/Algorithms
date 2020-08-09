import sys
sys.stdin = open("input.txt")


N = int(input())
result = []
# 100000 꼴로 만들어 줘야 함.
while True:
    # 끝자리가 1이다 -> 홀수다 못만들기 때문에 *2
    if N & 1:
        result += ['[/]']
        N = N * 2
    # 뒤에서 두번째 자리가 1이다 -> 없애 준다.
    elif N & 2:
        result += ['[+]']
        N = N -2
    else:
        result = result + ['[*]']
        N = N //2
    if N == 0:
        break

print(len(result))
print(*result[::-1])