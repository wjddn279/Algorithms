def solution(numbers, hand):
    answer = ''
    leftside, rightside = {1:(0,0),4:(1,0),7:(2,0)},{3:(0,2),6:(1,2),9:(2,2)}
    both = {2:(0,1),5:(1,1),8:(2,1),0:(3,1)}
    left,right = (3,0),(3,2)
    for number in numbers:
        if number in leftside:
            answer += 'L'
            left = leftside[number]
        elif number in rightside:
            answer += 'R'
            right = rightside[number]
        else:
            left_dis,right_dis = distance(left,both[number]),distance(right,both[number])
            if left_dis < right_dis:
                answer += 'L'
                left = both[number]
            elif left_dis > right_dis:
                answer += 'R'
                right = both[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    right = both[number]
                else:
                    answer += 'L'
                    left = both[number]
    return answer

def distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))