#Softeer level2 : 8단 변속기

gears = list(map(int, input().split()))

if gears == sorted(gears):
    print("ascending")
elif gears == sorted(gears, reverse=True):
    print("descending")
else:
    print("mixed")