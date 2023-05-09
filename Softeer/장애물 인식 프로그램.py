#Softeer level2 : 장애물 인식 프로그램

#지도의 크기 N
N = int(input())

#2차원 배열로 저장
aparts = []
for k in range(N):
    apart = list(map(int, input()))
    aparts.append(apart)

#시작 default 값
cnt = 2 #모여있는 장애물을 cnt값으로 바꿀거다.
buildings = {} #dictionary 형태로 모여있는 장애물의 수를 count

def makebuilding(i, j, cnt):
    '''
    1이라는 값을 찾으면 바이러스 퍼지듯이 같은 cnt값으로 배열을 바꿔주는 함수
    return 값은 없고, 그냥 같은 cnt값으로 바꿔준다
    '''
    #자기 자신에 대한 변형 cnt로
    if aparts[i][j] != cnt:
        aparts[i][j] = cnt
        buildings[cnt] += 1 #dictionary에 같은 cnt 몇개인지 count

    #위가 1이면 cnt로 변경
    if i > 0 and aparts[i-1][j] == 1:
        aparts[i-1][j] = cnt
        buildings[cnt] += 1

        makebuilding(i-1, j, cnt) #함수를 반복

    #아래가 1이면 cnt로 변경
    if i < N-1 and aparts[i+1][j] == 1:
        aparts[i+1][j] = cnt
        buildings[cnt] += 1

        makebuilding(i+1, j, cnt)

    #왼쪽이 1이면 cnt로 변경
    if j > 0 and aparts[i][j-1] == 1:
        aparts[i][j-1] = cnt
        buildings[cnt] += 1

        makebuilding(i, j-1, cnt)

    #오른쪽이 1이면 cnt로 변경
    if j < N-1 and aparts[i][j+1] == 1:
        aparts[i][j+1] = cnt
        buildings[cnt] += 1

        makebuilding(i, j+1, cnt)

#2차원 배열을 한 줄 한 줄 뜯어보기
for i in range(N):
    for j in range(N):
        if aparts[i][j] == 1:
            buildings[cnt] = 0

            makebuilding(i, j, cnt)

            cnt += 1 #이제 다음 모여있는 블럭 count

#총 몇개의 블럭인지 print
print(cnt-2)

#각각 블록의 개수 print
values = list(buildings.values())
values.sort()

for value in values:
    print(value)


