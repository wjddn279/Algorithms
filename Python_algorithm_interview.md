## 일일 온도

```python
# 입력 
T = [73,74,75,71,69,72,76,73]
# 결과
output = [1,1,4,2,1,1,0,0]
```

화씨 온도 리스트 T를 입력 받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지 출력하시오.

생각해야 하는 것 : 지금 결과를 내지 못하고 있는 값은 이때까지 그 값보다 큰 값이 나오지 않았다

-> 결과가 나오지 않은 것들을 순서대로 stack에 담아보면 내림차순이다.

-> 그렇다면 스택의 제일 마지막에 있는( stack[-1]) 값이 최소값이다.

-> 현재 온도가 stack[-1]보다도 작다면 당연히 다른 stack의 값들 보다도 작다.

-> 그 경우에는 순회를 할 필요가 없다는 것이다.

-> 반대로 stack[-1]보다 크다면  그 값을 pop 하여 현재 시간에서 빼면 답이고

-> 조건이 만족이 안 될때 까지 순회하여 pop 한다.

```python
T = [73,74,75,71,69,72,76,73]
# 결과
result = [0 for _ in range(len(T))]
stack = []
for idx,tem in enumerate(T):
    while stack and T[stack[-1]] < tem:
        mem = stack.pop()
        result[mem] = idx - mem
    stack.append(idx)

print(result)
```



