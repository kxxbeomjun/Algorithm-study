## Softeer - 현대자동차그룹 SW인재확보플랫폼 
### 문제들을 풀면서 느낀 점 & 참고할 점

#### Level 2
***
##### [금고털이](https://softeer.ai/practice/info.do?idx=1&eid=395)
+ 제출답안 : [금고털이.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/%EA%B8%88%EA%B3%A0%ED%84%B8%EC%9D%B4.py)
+ 여러줄에 걸친 input값을 한줄로 list에 append 할 수 있다.
+ Python 시간초과를 해결하기 위해서는 ```input()``` 대신 ```sys.stdin.readline()``` 사용하기
+ ```while``` loop 보다는 ```for``` 문에서의 break가 메모리를 더 절약한다.

##### [8단 변속기](https://www.softeer.ai/practice/info.do?idx=1&eid=408&sw_prbl_sbms_sn=181201)
+ 제출답안 : [8단 변속기.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/8%EB%8B%A8%20%EB%B3%80%EC%86%8D%EA%B8%B0.py)
+ 오름/내림 차순을 판단하는 문제
+ ```list```로 input을 받아서 ```sorted(list)```함수로 오름/내림 차순인지 판단

##### [장애물 인식 프로그램](https://www.softeer.ai/practice/info.do?idx=1&eid=409&sw_prbl_sbms_sn=181207)
+ 제출답안 : [장애물 인식 프로그램.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/%EC%9E%A5%EC%95%A0%EB%AC%BC%20%EC%9D%B8%EC%8B%9D%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8.py)
+ 엄청 엄청... 오래 풀었던 2차원 배열 문제
+ 내 코드내 ```makebuilding```이라는 함수에서 ```elif```가 아닌 ```if```문 만을 이용해야만 상하좌우 모두를 살핀다.
  + ```elif```를 사용하면 상하좌우 중 하나만 살피고 나머지에 대해서는 살피지 않는다.. elif의 특성
  + 각각을 살핀 후에 ```if```문 내에 함수를 다시 **recursion** 하는 코드를 넣어줘야한다.
+ ```cnt```값을 이용해서 서로 다른 블록으로 지정할 수 있다.

##### [전광판]([https://www.softeer.ai/practice/info.do?idx=1&eid=408&sw_prbl_sbms_sn=181201](https://www.softeer.ai/practice/info.do?idx=1&eid=624))
+ 제출답안 : [전광판.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/%EC%A0%84%EA%B4%91%ED%8C%90.py)
+ 21년 재직자 대회 예선 문제
+ 숫자들을 모두 ```dictionary```로 미리 설정해서 저장하는 것이 편하다
  + ```\```를 이용해서 여러줄로 나눠서 코드를 작성하는 것이 가독성과 찾기에 편하다.

#### Level 3
***
