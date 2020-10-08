## Bitmasking

- 비트마스킹의 의미? 활용?

```python
# 3차원 배열 visited = 10 * M * N의 메모리 활용
visited_array = [[[0 for _ in range(10)] for _ in range(M)] for _ in range(N)]
# bitmasking M*N 만큼의 메모리 활용
visited_bit = [[0 for _ in range(M)] for _ in range(N)]

# 그냥 방문 체크
visited_array[x][y][i] = 1
# 비트마스킹 방문 체크 -> 2진수의 i번째 자리를 1로 만듬
visited_bit[x][y] = visited_bit[x][y] | (1<<i)

# 그냥 방문 확인
if visited_array[x][y][i]:
# 비트마스킹 방문 확인 -> 2진수로 바꾸었을때 i번째 자리가 1인가 확인
if visited_array[x][y] & (1<<i)

# 꼭 visited 체크일때만 쓰이는건 아님 1,0의 배열을 하나의 숫자로 나타내는 것도 가능함
# ex) 35 = 010011 / [0,1,0,0,1,1] 과 같은 의미로 사용이 가능하다.
```

