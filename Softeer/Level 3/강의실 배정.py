#Softeer level3 강의실 배정.py

import sys
import heapq

N = int(sys.stdin.readline())
meeting_time = []

for _ in range(N):
    start, end = list(map(int, sys.stdin.readline().split()))
    # 끝나는 시간이 가장 작은 것을 맨 앞에 넣어준다, 만약 시작 시간이 같을 때에는 가장 작은 시간부터 오름차순으로
    heapq.heappush(meeting_time, (end, start))

end_time = 0
cnt = 0

while meeting_time:
    if meeting_time[0][1] >= end_time:
        end_time = heapq.heappop(meeting_time)[0]
        cnt += 1
        continue

    heapq.heappop(meeting_time)

print(cnt)



# 아래는 최초 작성했던 코드, lambda 때문에 시간초과 오류가 발생한다.
# import sys
#
# n = int(sys.stdin.readline())
#
# classes = []
# for _ in range(n):
#     start, end = map(int, sys.stdin.readline().split())
#     classes.append((start, end))
#
# classes.sort(key=lambda x: (x[1], x[0]))
# answer = 0
# now = 0
#
# for start, end in classes:
#     if now <= start:
#         answer += 1
#         now = end
#
# print(answer)



