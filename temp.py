
def prin(a):
    for i in a:
        print(i)
    print()

def radio(x,y,r):
    for idx,i in enumerate(range(x-r,x+r+1)):
        if idx <= r:
            for j in range(y-idx,y+idx+1):
                matrix[i][j] = 1
        else:
            for j in range(y-(2*r-idx),y+(2*r-idx)+1):
                matrix[i][j] = 1

matrix = [[0 for _ in range(5)] for _ in range(5)]
radio(2,2,2)
prin(matrix)
