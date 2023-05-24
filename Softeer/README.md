## Softeer - 현대자동차그룹 SW인재확보플랫폼 
### 문제들을 풀면서 느낀 점 & 참고할 점

#### Level 2
***
##### [금고털이](https://softeer.ai/practice/info.do?idx=1&eid=395)
+ 제출답안 : [금고털이.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/Level%202/%EA%B8%88%EA%B3%A0%ED%84%B8%EC%9D%B4.py)
+ 여러줄에 걸친 input값을 한줄로 list에 append 할 수 있다.
+ Python 시간초과를 해결하기 위해서는 ```input()``` 대신 ```sys.stdin.readline()``` 사용하기
+ ```while``` loop 보다는 ```for``` 문에서의 break가 메모리를 더 절약한다.

##### [8단 변속기](https://www.softeer.ai/practice/info.do?idx=1&eid=408&sw_prbl_sbms_sn=181201)
+ 제출답안 : [8단 변속기.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/Level%202/8%EB%8B%A8%20%EB%B3%80%EC%86%8D%EA%B8%B0.py)
+ 오름/내림 차순을 판단하는 문제
+ ```list```로 input을 받아서 ```sorted(list)```함수로 오름/내림 차순인지 판단

##### [장애물 인식 프로그램](https://www.softeer.ai/practice/info.do?idx=1&eid=409&sw_prbl_sbms_sn=181207)
+ 제출답안 : [장애물 인식 프로그램.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/Level%202/%EC%9E%A5%EC%95%A0%EB%AC%BC%20%EC%9D%B8%EC%8B%9D%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8.py)
+ 엄청 엄청... 오래 풀었던 2차원 배열 문제
+ 내 코드내 ```makebuilding```이라는 함수에서 ```elif```가 아닌 ```if```문 만을 이용해야만 상하좌우 모두를 살핀다.
  + ```elif```를 사용하면 상하좌우 중 하나만 살피고 나머지에 대해서는 살피지 않는다.. elif의 특성
  + 각각을 살핀 후에 ```if```문 내에 함수를 다시 **recursion** 하는 코드를 넣어줘야한다.
+ ```cnt```값을 이용해서 서로 다른 블록으로 지정할 수 있다.

##### [전광판](https://www.softeer.ai/practice/info.do?idx=1&eid=624)
+ 제출답안 : [전광판.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/Level%202/%EC%A0%84%EA%B4%91%ED%8C%90.py)
+ 21년 재직자 대회 예선 문제
+ 숫자들을 모두 ```dictionary```로 미리 설정해서 저장하는 것이 편하다
  + ```\```를 이용해서 여러줄로 나눠서 코드를 작성하는 것이 가독성과 찾기에 편하다.

##### [회의실 예약](https://www.softeer.ai/practice/info.do?idx=1&eid=626)
+ 제출답안 : [회의실 예약.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/Level%202/%ED%9A%8C%EC%9D%98%EC%8B%A4%20%EC%98%88%EC%95%BD.py)
+ 21년 재직자 대회 예선 문제, 출력 조건이 매우 까다로웠다.
+ ```dictionary[key] = [[i,i+1] for i in range(9,18)]```를 활용하면 시간대별로 default 값을 저장할 수 있다.

##### [비밀메뉴](https://www.softeer.ai/practice/info.do?idx=1&eid=623&sw_prbl_sbms_sn=181299)
+ 제출답안 : [비밀메뉴.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/Level%202/%EB%B9%84%EB%B0%80%EB%A9%94%EB%89%B4.py)
+ 21년 재직자 대회 예선 문제
+ ```A = input().split()```의 형에 대한 이해
  + ```1 2 3 4```같은 input을 받으면 ```A```는 **list**형태로 저장된다. 
  + ```A```는 ```['1', '2', '3', '4']```로 저장된다. 

##### [GBC](https://www.softeer.ai/practice/info.do?idx=1&eid=584)
+ 제출답안 : [GBC.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/Level%202/GBC.py)
+ 각각의 구간을 ```section = [list(map(int, input().split())) for _ in range(N)]``` method를 이용하여 저장했다.
+ ```pop``` method를 이용해서 이미 확인한 구간을 날려버리고, 새롭게 구간을 저장하는 것이 **key** 였다.



#### Level 3
***
##### [코딩 테스트 세트](https://www.softeer.ai/practice/info.do?idx=1&eid=630)
+ 제출답안 : [코딩 테스트 세트.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/Level%203/%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EC%84%B8%ED%8A%B8.py)
+ 정답설명 : [코딩 테스트 세트 YOUTUBE](https://www.youtube.com/watch?v=-xp1Pc6_lIc)
+ 주어진 input 숫자의 범위가 너무 커서 ```이진 탐색(Binary search)```를 사용해야한다.
  + 함수안에 함수 return문을 넣어서 계속 절반으로 탐색 범위를 줄이는 방법

##### [로봇이 지나간 경로](https://www.softeer.ai/practice/info.do?idx=1&eid=577&sw_prbl_sbms_sn=204500)
+ 제출답안 : [로봇이 지나간 경로.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/Level%203/%EB%A1%9C%EB%B4%87%EC%9D%B4%20%EC%A7%80%EB%82%98%EA%B0%84%20%EA%B2%BD%EB%A1%9C.py)
+ 너무너무너무 **오래푼 문제**
+ ```BFS / DFS``` 개념을 사용하는 문제
+ 주석처리까지 잘 써놨으니 꼭 한번 다시 읽어보기
