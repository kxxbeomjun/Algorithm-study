#Softeer lever2 : 금고털이

#W: 배낭의 무게, N개의 귀금속 종류
W, N = map(int, input().split())

#jewelry 라는 list를 만들어서 금속의 무게와, 무게당 가격을 append한다.
jewelry = []
for k in range(N):
    weight, price = map(int, input().split())
    jewelry.append([weight, price])

#jewelry의 sublist 1번째 index가 무게당 가격이므로 해당 값을 기준으로 내림차순으로 정렬했다.
sorted_jewelry = sorted(jewelry, key=lambda x : x[1], reverse=True)

total_price = 0
for weight, price in sorted_jewelry:
    if W > weight:
        total_price += weight * price
        W -= weight
    else:
        total_price += W * price
        break

print(total_price)

