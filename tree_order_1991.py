import sys
sys.stdin = open("input.txt")

def order(root):

    pre_order.append(root)
    left,right = dic[root][0], dic[root][1]
    if left != '.':
        order(left)
    in_order.append(root)
    if right != '.':
        order(right)
    post_order.append(root)
N = int(input())
dic = {}
for i in range(N):
    a,b,c = input().split()
    if i == 0:
        start = a
    dic[a] = [b,c]
pre_order, in_order, post_order = [], [], []
order(start)
print(''.join(pre_order))
print(''.join(in_order))
print(''.join(post_order))