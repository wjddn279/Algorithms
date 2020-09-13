from _collections import deque

def solution(cards):
    answer = 0
    cards = deque(cards)

    def game():
        global sum_me,sum_you
        me,you = [], []
        me_flag,you_flag = False,False
        flag = False
        turn = 0
        while cards:
            turn += 1
            card = cards.popleft()
            if card > 10:
                card = 10
            if turn == 1 or turn == 3:
                me.append(card)
                continue
            if turn == 2:
                you.append(card)
                continue
            if turn == 4:
                you.append(card)
                if (sum(me) == 21 or me ==[1,10] or me == [10,1]):
                    if sum(you) == 21:
                        return 0
                    else:
                        return 3
                if (sum(you) == 21 or you ==[1,10] or you == [10,1]):
                    return -2
                else:
                    continue

            if sum(me) > 21:
                return -2

            if you[1] == 1 or you[1]>6:
                if sum(me) < 17:
                    me.append(card)
                    if sum(me) > 21:
                        return -2
                else:
                    flag = True
            if you[1] == 2 or you[1] == 3:
                if sum(me) < 12:
                    me.append(card)
                    if sum(me) > 21:
                        return -2
                else:
                    flag = True
            else:
                flag = True

            if flag:
                if sum(you) > 21:
                    return 2
                if sum(you) < 17:
                    you.append(card)
                    if sum(you) > 21:
                        return 2
                if 17 <= sum(you) <= 21:
                    you_flag = True
            if you_flag:
                sum_me,sum_you = [],[]
                rec1(len(me),0,me,0)
                rec2(len(you),0,you,0)
                a,b = min(sum_me),min(sum_you)
                if a == b:
                    return 0
                # 내 승리
                elif a < b:
                    return 2
                else:
                    return -2
        return 0

    def rec1(n,k,arr,sum):
        global sum_me
        if n == k:
            if sum < 21:
                sum_me.append(21-sum)
        else:
            if arr[k] != 1:
                rec1(n,k+1,arr,sum+arr[k])
            else:
                rec1(n, k + 1, arr, sum + 1)
                rec1(n, k + 1, arr, sum + 11)

    def rec2(n,k,arr,sum):
        global sum_you
        if n == k:
            if sum < 21:
                sum_you.append(21-sum)
        else:
            if arr[k] != 1:
                rec2(n,k+1,arr,sum+arr[k])
            else:
                rec2(n, k + 1, arr, sum + 1)
                rec2(n, k + 1, arr, sum + 11)

    while cards:
        answer += game()
    return answer

print(solution([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))

# 처음 나 한장 딜러 한장 나 한장 딜러 한장 총 4장 기본 세팅

# 두개 합이 21이다? -> 카드 받지 않고 딜러 카드 확인
# 딜러가 블랙잭이다 -> 무승부
# 딜러가 블랙잭이 아니다 -> +3



# -> 더이상 안받으면 딜러 카드 공개 (현재 내가 갖는 패는 21 이하)
# 딜러 합이 21 보다 크다? -> 내 승리 + 2
# 딜러 합이 21 이다? -> 블랙잭 패배 -3
# 아무것도 아니다? -> 합이 17이상일때 까지 계속 받고 21 이상되면 패배

# 안끝난 경우 카드 합이 21에 가까운 사람이 이김
# 두개 합이 21 이상이다? -> 플레이어가 즉시 패배

# 도중에 카드없으면 무승부

# -> 더이상 안받으면 딜러 카드 공개 (현재 내가 갖는 패는 21 이하)
# 딜러 합이 21 보다 크다? -> 내 승리 + 2
# 딜러 합이 21 이다? -> 블랙잭 패배 -3
# 아무것도 아니다? -> 합이 17이상일때 까지 계속 받고 21 이상되면 패배


# 안끝난 경우 카드 합이 21에 가까운 사람이 이김
# 두개 합이 21 이상이다? -> 플레이어가 즉시 패배

# 도중에 카드없으면 무승부