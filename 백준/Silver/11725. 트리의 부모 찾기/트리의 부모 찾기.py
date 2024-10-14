import sys
from sys import setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())

visit = [False] * (N + 1)
tree = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0] * (N + 1)
def find(node):
    visit[node] = True
    node_list = tree[node]
    for child in node_list:
        if not visit[child]:
            parents[child] = node
            find(child)
find(1)
print('\n'.join(map(str, parents[2:])))