import sys
sys.stdin = open("gostack_3425.txt")

from _collections import deque

def deter(com):
    # com : 명령어
    if com[0] == 'NUM':
        stack.append(int(com[1]))
    elif com[0] == 'POP':
        if len(stack) == 0:
            return -1
        else:
            stack.pop()
    elif com[0] == 'INV':
        if len(stack) == 0:
            return -1
        else:
            stack[-1] = -stack[-1]
            if abs(stack[0]) > pow(10,9):
                return -1
    elif com[0] == 'DUP':
        if len(stack) == 0:
            return -1
        else:
            # 확실할려나
            temp = stack[-1]
            stack.append(temp)
    elif com[0] == 'SWP':
        if len(stack) < 2:
            return -1
        else:
            length = len(stack)
            stack[length-1],stack[length-2] = stack[length-2],stack[length-1]
    elif com[0] == 'ADD':
        if len(stack) < 2:
            return -1
        else:
            a = stack.pop()
            b = stack.pop()
            result = a + b
            if abs(result) > pow(10,9):
                return -1
            else:
                stack.append(result)
    elif com[0] == 'SUB':
        if len(stack) < 2:
            return -1
        else:
            a = stack.pop()
            b = stack.pop()
            result = b - a
            if abs(result) > pow(10,9):
                return -1
            else:
                stack.append(result)
    elif com[0] == 'MUL':
        if len(stack) < 2:
            return -1
        else:
            a = stack.pop()
            b = stack.pop()
            result = a * b
            if abs(result) > pow(10,9):
                return -1
            else:
                stack.append(result)
    elif com[0] == 'DIV':
        if len(stack) < 2:
            return -1
        else:
            # 첫번째
            a = stack.pop()
            # 두번째
            b = stack.pop()
            if a == 0:
                return -1
            result = abs(b)//abs(a)
            if abs(result) > pow(10,9):
                return -1
            else:
                if a > 0 and b < 0:
                    result = - abs(result)
                elif a < 0 and b > 0:
                    result = - abs(result)
                stack.append(result)
    elif com[0] == 'MOD':
        if len(stack) < 2:
            return -1
        else:
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                return -1
            result = abs(b)%abs(a)
            if abs(result) > pow(10,9):
                return -1
            else:
                if b < 0:
                    result = - abs(result)
                else:
                    result = abs(result)
                stack.append(result)
while True:
    flag = True
    first = list(input().split())
    command = []
    numbers = []
    if first == ['QUIT']:
        break
    elif first == ['END']:
        flag = False
    else:
        command.append(first)
    while flag:
        temp = list(input().split())
        if temp == ['END']:
            break
        else:
            command.append(temp)
    T = int(input())
    for i in range(T):
        numbers.append((int(input())))
    _ = input()
    for number in numbers:
        number = int(number)
        stack = [number]
        for com in command:
            result = deter(com)
            print(stack)
            if result == -1:
                print('ERROR')
                break
        else:
            if len(stack) != 1:
                print('ERROR')
            else:
                print(*stack)
    print()
