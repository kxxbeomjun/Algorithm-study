#Softeer level3 로봇이 지나간 경로

import sys
from collections import deque

h, w = map(int, sys.stdin.readline().split()) #h개의 행 w개의 열
matrix = [list(sys.stdin.readline().strip()) for _ in range(h)]
#list로 matrix만들기 matrix는 0,0이 왼쪽 위 최상단 꼭짓점

dx = [-1,0,1,0] #위, 아래로 움직이는 경우
dy = [0,-1,0,1] #왼, 오로 움직이는 경우
directionMark = ['^','<','v','>'] #방향을 말해주는 거


def findDirection(x,y):
    '''
    x,y 방향을 input받으면 방향을 찾아주는 함수
    '''
    cnt = 0
    for i in range(4): #index 0:위, 1:왼, 2:아래, 3:오
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w and  matrix[nx][ny] == "#": #범위에 있는지 따지고, #이 있으면
            direction = i
            cnt += 1
    return (direction if cnt == 1 else -1) #시작 or 끝점이 아닌 경우 -1 return

def findStart(matrix):
    '''
    Matirx를 input으로 받고, 스타트 지점을 찾아주는 함수
    시작지점의 x,y값 그리고 방향의 index를 return
    '''
    for x in range(h):
        for y in range(w):
            if matrix[x][y] == "#":
                direction = findDirection(x,y)
                if direction != -1:
                    #시작점이나 끝점이 아닌경우는 방향이 두개있을수있다 그때는 -1 return하도록
                    return x,y,direction

def navigate(x,y,direction):
    preDir = newDir = direction
    matrix[x][y] = "."
    while True:
        while newDir == preDir: #직진
            print('A', end="")
            x,y = x+dx[newDir], y+dy[newDir]
            matrix[x][y] = "."
            x,y = x+dx[newDir], y+dy[newDir]
            matrix[x][y] = "." #두칸 간 것이다.

            preDir = newDir #이전위치가 새로운위치로 업데이트하고
            newDir = findDirection(x, y)  #새롭게 탐색해준다.
        if newDir == -1:
            # newDir가 -1이라는거는 findDirection 함수에서 else return문으로 더이상 갈 방향이 없다는 의미
            # while loop 탈출 및 negivate 함수 종료
            return
        elif (newDir - preDir) % 4 == 1:
            print('L', end="")
        elif (newDir - preDir) % 4 == 3:
            print('R', end="")
        preDir = newDir


x,y,direction = findStart(matrix)
print(x+1, y+1) #최초 시작하는 위치
print(directionMark[direction]) #최초 시작하는 방향
navigate(x,y,direction)



