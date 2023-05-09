#Softeer level2: 21년 재직자 대회 예선 전광판

number ={'0':'1110111', \
         '1':'0010010', \
         '2':'1011101', \
         '3':'1011011', \
         '4':'0111010', \
         '5':'1101011', \
         '6':'1101111', \
         '7':'1110010', \
         '8':'1111111', \
         '9':'1111011', \
         ' ':'0000000'}

#test case 의 개수 T
T = int(input())

for _ in range(T):
    a, b = input().split()

    a = (5-len(a)) * ' ' + a
    b = (5-len(b)) * ' ' + b

    #다른 것의 개수 count해서 프린트
    total = 0
    for i in range(5):
        for j in range(7):
            total += (number[a[i]][j] != number[b[i]][j])

    print(total)


