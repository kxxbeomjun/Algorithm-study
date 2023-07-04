import sys

n, k = map(int, input().split()) #n개의 입력, k개의 색
colors = [[] for _ in range(k+1)]

for _ in range(n):
    x, y, k = map(int, input().split())
    colors[k].append([x, y]) #colors list에 x,y좌표들 저장

def dfs(num, min_x, max_x, min_y, max_y):
    global minArea

    if num > k:
        if minArea > (max_x-min_x) * (max_y-min_y):
            minArea = (max_x-min_x) * (max_y-min_y)
        return

    for color in colors[num]:
        x1, x2 = min(min_x, color[0]), max(max_x, color[0]) #x1, x2는 직사각형의 왼쪽, 오른쪽 x좌표
        y1, y2 = min(min_y, color[1]), max(max_y, color[1]) #y1, y2는 직사각형의 아래, 위 y좌표
        if minArea > (x2-x1) * (y2-y1): #코드의 효율성을 위해서 조건을 충족할 때만 다음 단계로 넘어가기
            dfs(num+1, x1, x2, y1, y2)
    return

minArea = 2000 * 2000 #이게 Area가 가질 수 있는 가장 큰 값
dfs(1, 1000, -1000, 1000, -1000)
print(minArea)