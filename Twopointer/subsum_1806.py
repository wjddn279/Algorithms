import sys
sys.stdin = open("subsum_1806.txt")

N, S = map(int,input().split())
matrix = list(map(int,input().split()))

start, end = 0, 0
sub_sum = matrix[0]
result = N+1
while True:
    if start == end:
        # result 가 1이 되어버리면 뒤에것 볼 필요 없음
        if sub_sum >= S:
            result = 1
            break
        # 둘 다 끝에 도달하면 break
        if end == N - 1 and start == N - 1:
            break
        # 아니라면 end를 한칸 앞으로 보내야 함
        else:
            end += 1
            sub_sum += matrix[end]
    # 부분합이 기준보다 크면 start를 앞으로 한칸 땡겨주고 부분합에서 전에 값 빼줌
    elif S <= sub_sum:
        result = min(result,end-start+1)
        sub_sum -= matrix[start]
        start += 1
    # 부분합이 기준보다 작다면 end를 앞으로 한칸 땡겨주고 부분합에서 나중 값 더해줌
    else:
        if end < N-1:
            end += 1
            sub_sum += matrix[end]
        # 만일 end가 N-1에 도착했지만 start는 도달 못했을 경우고 기준 값보다 작다?
        # start를 끝까지 땡겨줄 필요도 없이 끝내도 됨, 어차피 부분합은 작아지기만 하기때문
        else:
            break
if result == N+1:
    print(0)
else:
    print(result)