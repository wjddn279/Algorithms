def solution(arr):
    answer = [0,0]
    def check(arr,label):
        for i in arr:
            for num in i:
                if num != label:
                    return False
        return True
    def search(arr):
        if check(arr,1):
            answer[1] += 1
            return
        if check(arr,0):
            answer[0] += 1
            return
        N = len(arr)//2
        search([arr[i][0:N] for i in range(N)])
        search([arr[i][N:2*N] for i in range(N)])
        search([arr[i][0:N] for i in range(N,2*N)])
        search([arr[i][N:2 * N] for i in range(N,2*N)])
    search(arr)
    return answer

solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])