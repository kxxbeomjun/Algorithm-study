import sys


def test(testSets):
    now = C[0]
    for i in range(N - 1):
        if now >= testSets:
            now = C[i + 1] + D[i]
        elif now + D[i] >= testSets:
            now = C[i + 1] + (now + D[i] - testSets)
        else:
            return False
    if now >= testSets:
        return True
    else:
        return False


def Bsearch(start, end):
    if start == end:
        return start
    mid = (start + end + 1) // 2
    if test(mid):
        return Bsearch(mid, end)
    else:
        return Bsearch(start, mid - 1)


N, T = map(int, input().split())
for _ in range(T):
    Questions = list(map(int, input().split()))
    C = []
    D = []
    for i in range(N - 1):
        C.append(Questions[2 * i])
        D.append(Questions[2 * i + 1])

    C.append(Questions[2 * (N - 1)])

    print(Bsearch(0, 2 * 10 ** 12))