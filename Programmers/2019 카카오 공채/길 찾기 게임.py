# import heapq
# def solution(nodeinfo):
#     answer = [[]]
#     new = []
#     for idx,node in enumerate(nodeinfo):
#         new.append([node[1],-node[0],idx+1])
#     new.sort(reverse=True)
#     tree = [[-new[i][1],new[i][0],new[i][2]] for i in range(3)]
#     print(tree)
#     idx = 1
#     while idx < len(new):
#         print(tree)
#         x,y,num = -new[idx][1],new[idx][0],new[idx][2]
#         if not tree[(len(tree)-1)//2]:
#             tree.append(None)
#             continue
#         root_x,root_y,root_num = tree[(len(tree)-1)//2]
#         rr_x,rr_y,rr_num = tree[((len(tree)-1)//2 -1)//2]
#         if len(tree)%2:
#             if rr_x < x < root_x:
#                 tree.append([x,y,num])
#                 idx += 1
#             else:
#                 tree.append(None)
#         else:
#             if root_x < x < rr_x:
#                 tree.append([x,y,num])
#                 idx += 1
#             else:
#                 tree.append(None)
#     print(new)
#     print(tree)
#     return answer


def solution(nodeinfo):
    def find_root(nodeInfo):
        root_y = -1
        max_i = -1
        for i in range(len(nodeInfo)):
            if root_y < nodeInfo[i][1]:
                root_y = nodeInfo[i][1]
                max_i = i
        return nodeInfo[max_i][2], max_i

    def orders(my_list):
        nonlocal preorder, postorder
        if my_list:
            num, idx = find_root(my_list)
            preorder.append(num)  # 전위
            orders(my_list[:idx])
            orders(my_list[idx+1:])
            postorder.append(num)  # 후위


    my_list = [[nodeinfo[i][0], nodeinfo[i][1], i + 1] for i in range(len(nodeinfo))]
    my_list.sort(key=lambda x: x[0])
    print(my_list)
    preorder, postorder = [], []
    orders(my_list)
    return [preorder, postorder]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))