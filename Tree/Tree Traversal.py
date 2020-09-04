tree = ['F','B','G','A','D',None,'I',None,None,'C','E',None,None,'H']
pre_path = []
post_path = []
in_path = []
def preorder(root):
    if root >= len(tree) or not tree[root]:
        return
    pre_path.append(tree[root])
    left = 2 * root + 1
    right = 2 * root + 2
    preorder(left)
    preorder(right)

def postorder(root):
    if root >= len(tree) or not tree[root]:
        return
    left = 2 * root + 1
    right = 2 * root + 2
    postorder(left)
    postorder(right)
    post_path.append(tree[root])

def inorder(root):
    if root >= len(tree) or not tree[root]:
        return
    left = 2 * root + 1
    right = 2 * root + 2
    inorder(left)
    in_path.append(tree[root])
    inorder(right)

preorder(0)
postorder(0)
inorder(0)
print(pre_path)
print(post_path)
print(in_path)
print()