import sys
sys.stdin = open("input.txt")

N, M, D = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]

