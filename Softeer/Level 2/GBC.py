#Softeer level2 GBC

# N : 구간의 길이 / M : 테스트 하는 구간의 개수
N, M = map(int, input().split())

N_section = [list(map(int, input().split())) for _ in range(N)]
M_section = [list(map(int, input().split())) for _ in range(M)]

total = 0
max_diff = []

while True:
    if N_section == [] or M_section == []:
        break #while문 escape

    diff_length = M_section[0][0] - N_section[0][0] #구간의 길이 차이 정의

    if diff_length > 0:
        max_diff.append(M_section[0][1] - N_section[0][1]) #해당 구간에서의 속도 차이
        N_section.pop(0) #이미 판단한 N_section 처음 날리기
        M_section[0][0] = -diff_length

    elif diff_length < 0:
        max_diff.append(M_section[0][1] - N_section[0][1])
        M_section.pop(0)
        N_section[0][0] = -diff_length

    else: #길이차이가 같은 경우
        max_diff.append(M_section[0][1] - N_section[0][1])
        M_section.pop(0)
        N_section.pop(0)


if max(max_diff) > 0:
    print(max(max_diff))

else: #max_diff가 음수면 즉, 제한 속도를 벗어나지 않은 경우 0을 출력한다.
    print(0)

