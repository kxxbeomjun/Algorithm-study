#Softeer 21년 재직자 예선 - 회의실 예약

#회의실의 개수 N, 예약된 회의의 수 M
N, M = map(int,input().split())

#회의실을 저장할 dictionary 형성
conference_room ={}
for _ in range(N):
    room_name = input()
    conference_room[room_name] = [[i,i+1] for i in range(9,18)]

for _ in range(M):
    name, st, et = input().split() #회의실 이름, 시작시간, 종료시간

    for i in range(int(st), int(et)):
        if [i, i+1] not in conference_room[name]:
            pass
        else:
            conference_room[name].remove([i, i+1])

for value in sorted(conference_room):
    if len(conference_room[value]) == 0: #예약이 불가능 한 경우
        print("Room " + value + ":")
        print("Not available")

        if value == sorted(conference_room.keys())[-1]:  # 마지막 value면 하이폰 다섯개를 출력을 안하고 종료
            break

        else:
            print("-----")  # 마지막 value가 아니라면 하이폰 다섯개 출력

        continue  # 다음 value값으로

    else:  # 회의실 예약이 다 차지 않았을 경우
        tmp = []  # 임시
        answer = []
        for i in range(len(conference_room[value])):
            if len(conference_room[value]) == 1:  # 회의 예약이 가능한 시간이 딱 하나만 있을 경우
                tmp.append(conference_room[value][i])

            # 회의 예약이 가능한 시간이 여러 개 일 경우
            if i == len(conference_room[value]) - 1:  # IndexError를 방지하기 위해 따로 선언
                tmp.append(conference_room[value][i])

            elif 0 <= i < len(conference_room[value]) - 1:
                # 현재 회의가 끝나는 시간이랑 다음 회의가 시작하는 시간이랑 같을 때
                if conference_room[value][i][1] == conference_room[value][i + 1][0]:
                    tmp.append(conference_room[value][i])

                else:
                    tmp.append(conference_room[value][i])
                    answer.append([tmp[0][0], tmp[-1][1]])
                    tmp = []

        if tmp == []:
            pass

        else:
            answer.append([tmp[0][0], tmp[-1][1]])  # 회의예약이 가능한 구간의 시작시간이랑 끝나는 시간을 넣어준다

        print("Room " + value + ":")
        print(len(answer), "available:")
        for i in range(len(answer)):
            if answer[i][0] == 9:
                answer[i][0] = "09"  # 9는 앞에 0을 붙혀서 출력
                print(answer[i][0] + "-" + str(answer[i][1]))

            else:
                print(str(answer[i][0]) + "-" + str(answer[i][1]))

        if value == sorted(conference_room.keys())[-1]:
            break

        else:
            print("-----")
