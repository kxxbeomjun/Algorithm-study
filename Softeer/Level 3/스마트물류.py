import sys

N, K = map(int, input().split()) #N: 라인의 길이, K: 로봇가능거리

#P,H 행렬 P:로봇, H:부품
place = list(sys.stdin.readline().strip())

cnt = 0 #로봇이 처리한 물류 갯수를 셀 parameter

#for loop를 이용해서 왼쪽부터 물류를 찾는다.
for i in range(N):
    if place[i] == "P":
        #로봇의 위치에서 앞뒤로 K만큼의 거리 중 부품을 찾는다
        for j in range(i-K, i+K+1):
            if j<0 or j>N-1: #부품이 집는 거리가 라인의 거리안에 있도록
                continue
            elif place[j] == "H":
                cnt += 1
                place[j] = "Done" #다른걸로 바꿔서 재탐색이 안되게
                break

print(cnt)

