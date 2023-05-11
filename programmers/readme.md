## 프로그래머스
***
**C++ 언어를 이용하여, 코딩 테스트를 준비해보았다.**

#### [x만큼 간격이 있는 n개의 숫자](https://school.programmers.co.kr/learn/courses/30/lessons/12954?language=cpp) 
+ 제출답안 : [x만큼 간격이 있는 n개의 숫자.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/x%EB%A7%8C%ED%81%BC%20%EA%B0%84%EA%B2%A9%EC%9D%B4%20%EC%9E%88%EB%8A%94%20n%EA%B0%9C%EC%9D%98%20%EC%88%AB%EC%9E%90.cpp)
+ ```vector``` 클래스의 주요한 method -> vector 클래스는 python의 list와 같은 배열 형태
  + ```push_back()```: vector의 끝에 새로운 원소를 추가합니다.
  + ```pop_back()```: vector의 끝에서 원소를 제거합니다.
  + ```size()```: vector에 포함된 원소의 개수를 반환합니다.
  + ```empty()```: vector가 비어있는지 확인합니다.
  + ```clear()```: vector의 모든 원소를 제거합니다.
  + ```erase()```: vector에서 원소를 제거합니다.
  + ```begin()```: vector의 첫 번째 원소를 가리키는 반복자를 반환합니다.
  + ```end()```: vector의 마지막 원소 다음을 가리키는 반복자를 반환합니다.
  + ```at()```: 인덱스를 이용하여 vector의 원소에 접근합니다.
+ **C++** 에서는 ```if / for / while```문 뒤에 ```()```로 조건을 표시한다.


#### [문자열 내 p와 y의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/12916)
+ 제출단안 : [문자열 내 p와 y의 개수.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%82%B4%20p%EC%99%80%20y%EC%9D%98%20%EA%B0%9C%EC%88%98.cpp)
+ ```and / or```은 **C++** 에서는 ```&& / ||``` 로 표현한다.
+ ```if / else if```는 ```{}```로 각각 묶어 가독성과 수정 편리성을 높인다.

#### [정수 제곱근 판별](https://school.programmers.co.kr/learn/courses/30/lessons/12934)
+ 제출답안 : [정수 제곱근 판별.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/%EC%A0%95%EC%88%98%20%EC%A0%9C%EA%B3%B1%EA%B7%BC%20%ED%8C%90%EB%B3%84.cpp)
+ ```#include <cmath>```헤더 파일 통해서 계산 시간을 줄일 수 있다.
  + ```sqrt(x)```: x의 제곱근을 반환합니다.
  + ```pow(x, y)```: x의 y 거듭제곱을 반환합니다.
  + ```sin(x)```: x의 사인 값을 반환합니다. (x는 라디안)
  + ```cos(x)```: x의 코사인 값을 반환합니다. (x는 라디안)
  + ```tan(x)```: x의 탄젠트 값을 반환합니다. (x는 라디안)
  + ```log(x)```: x의 자연로그 값을 반환합니다.
  + ```exp(x)```: e의 x 거듭제곱을 반환합니다.

#### [문자열을 정수로 바꾸기](https://school.programmers.co.kr/learn/courses/30/lessons/12925?language=cpp)
+ 제출답안 : [문자열을 정수로 바꾸기.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%84%20%EC%A0%95%EC%88%98%EB%A1%9C%20%EB%B0%94%EA%BE%B8%EA%B8%B0.cpp)
+ 자료형을 변형해주는 함수는 다양하다.
  + ```atoi```: 문자열을 정수로 변환하는 함수입니다. ```<cstdlib>``` 헤더 파일에 선언되어 있습니다. 
    + 예시: int num = atoi("123");
  + ```atof```: 문자열을 실수로 변환하는 함수입니다. ```<cstdlib>``` 헤더 파일에 선언되어 있습니다. 
    + 예시: double num = atof("1.23");
  + ```stod```: 문자열을 double 형태로 변환하는 함수입니다. ```<string>``` 헤더 파일에 선언되어 있습니다. 
    + 예시: double num = stod("1.23");
  + ```stof```: 문자열을 float 형태로 변환하는 함수입니다. ```<string>``` 헤더 파일에 선언되어 있습니다.
    + 예시: float num = stof("1.23");
  + ```stoi```: 문자열을 int 형태로 변환하는 함수입니다. ```<string>``` 헤더 파일에 선언되어 있습니다. 
    + 예시: int num = stoi("123");
