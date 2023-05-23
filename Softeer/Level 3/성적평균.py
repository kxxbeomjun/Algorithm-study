# Softeer level3 성적평균.py

# N: 학생 수, K: 구간 수
N, K = map(int, input().split())

# 학생들의 점수를 저장
scores = list(map(int, input().split()))

# 평균을 저장할 빈 list
averages = []
for i in range(K):
    start, end = map(int, input().split())

    tmp_sum = 0
    for k in range(start - 1, end):
        tmp_sum += scores[k]

    tmp_sum /= end - start + 1
    averages.append(format(tmp_sum, '.2f'))

for average in averages:
    print(average)


#다른 풀이도 있다.
# import sys
#
# #N, K를 받는 것
# N, K = map(int, input().split())
#
# #점수들을 받아서 list에 저장
# score = list(map(int, sys.stdin.readline().split()))
#
# #출력할 범위 들을 받아서 list안에 list로 형성
# range_list = [list(map(int, sys.stdin.readline().split())) for _ in range(K) ]
#
# #범위 별로 출력
# for i in range(K):
#     cut_score = score[range_list[i][0]-1:range_list[i][1]]
#     result = sum((cut_score))/len(cut_score)
#     result = format(result, '.2f')
#     print(result)