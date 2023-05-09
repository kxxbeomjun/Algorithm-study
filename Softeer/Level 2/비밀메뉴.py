#Softeer level2 비밀메뉴

#M: 조작법수 N: 누르는버튼수 K:총버튼수
M, N, K = map(int, input().split())
secret_menu = input().split() #길이 = M
user_menu = input().split() #길이 = N

boolean_flag = False
for k in range(N):
    if secret_menu == user_menu[k:k+M]: #slicing method 사용
        boolean_flag = True
        break

if boolean_flag:
    print('secret')
else:
    print('normal')