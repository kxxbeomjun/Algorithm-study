## Softeer - 현대자동차그룹 SW인재확보플랫폼 
### 문제들을 풀면서 느낀 점 & 참고할 점

#### Level 2
***
##### [금고털이](https://softeer.ai/practice/info.do?idx=1&eid=395)
+ 제출답안 : [금고털이.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/%EA%B8%88%EA%B3%A0%ED%84%B8%EC%9D%B4.py)
+ 여러줄에 걸친 input값을 한줄로 list에 append 할 수 있다.
+ Python 시간초과를 해결하기 위해서는 ```input()``` 대신 ```sys.stdin.readline()``` 사용하기
+ ```while``` loop 보다는 ```for``` 문에서의 break가 메모리를 더 절약한다.


#### Level 3
***
##### [8단 변속기](https://www.softeer.ai/practice/info.do?idx=1&eid=408&sw_prbl_sbms_sn=181201)
+ 제출답안 : [8단 변속기.py](https://github.com/kxxbeomjun/Algorithm-study/blob/main/Softeer/8%EB%8B%A8%20%EB%B3%80%EC%86%8D%EA%B8%B0.py)
+ 오름/내림 차순을 판단하는 문제
+ ```list```로 input을 받아서 ```sorted(list)```함수로 오름/내림 차순인지 판단
