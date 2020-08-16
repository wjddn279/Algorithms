import sys
sys.stdin = open("input.txt")

N = int(input())
data = [[] for _ in range(2001)]
for i in range(N):
    color,size = map(int,input().split())
    data[size].append((color,i))
result = [0 for _ in range(N)]
color_sum = [0 for _ in range(N+1)]
total_sum = 0
for size,arr in enumerate(data):
    temp,temp_size = {},0
    for color,idx in arr:
        if color in temp:
            result[idx] = total_sum - temp[color]
        else:
            result[idx] = total_sum - color_sum[color]
            temp[color] = color_sum[color]
        color_sum[color] += size
        temp_size += size
    total_sum += temp_size

for num in result:
    print(num)


