## 프로그래머스
**C++ 언어를 이용하여, 코딩 테스트를 준비하면서 기초 문법부터 기억할 내용까지 적어보았다.**
***

#### [직사각형 별찍기](https://school.programmers.co.kr/learn/courses/30/lessons/12969?language=cpp)
+ 제출답안 : [직사각형 별찍기.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95%20%EB%B3%84%EC%B0%8D%EA%B8%B0.cpp)
+ ```cin >>```에 대한 이해
  + C언어의 ```scanf```와 다르게 ```cin```에서는 입력받을 데이터 타입을 알려주는 **서식 문자열 %d, %c같은 것이 필요 없다.**
  + 또 주소를 나타내는 **주소 연산자 &도 필요가 없다.**
+ ```cout <<``` 에 대한 이해
  + python과 다르게 ```cout```은 **개행문자 ```\n```을 포함하지 않는다.**
    + 해결방법1 ```cout << "cout 개행1" << "\n";```
    + 해결방법2 ```cout << "cout 개행2\n";```
    + 해결방법3 ```cout << "cout 개행3 " << endl;```

#### [비밀지도](https://school.programmers.co.kr/learn/courses/30/lessons/17681)
+ 제출답안 : [비밀지도.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/%EB%B9%84%EB%B0%80%EC%A7%80%EB%8F%84.cpp)
+ ```|```는 비트 연산자로 이진법으로 덧셈된 값을 다시 십진법으로 바꾼수 
  + ex) arr1[i]가 5(이진수: 101), arr2[i]가 3(이진수: 011)인 경우, arr1[i] | arr2[i]는 7(이진수: 111)가 된다.
+ ```int/long/longlong```의 차이
  + **```int```는 10자리, ```long```은 19자리, ```long long```은 그보다 큰 정수**를 다룰때 type 정의 

#### [2016년](https://school.programmers.co.kr/learn/courses/30/lessons/12901)
+ 제출답안 : [2016년.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/2016%EB%85%84.cpp)
+ 문자열, 정수 배열의 길이를 미리 지정해서 저장 가능
  + ```string day[7] = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};```
  + ```int month[13] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};```

#### [x만큼 간격이 있는 n개의 숫자](https://school.programmers.co.kr/learn/courses/30/lessons/12954?language=cpp) 
+ 제출답안 : [x만큼 간격이 있는 n개의 숫자.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/x%EB%A7%8C%ED%81%BC%20%EA%B0%84%EA%B2%A9%EC%9D%B4%20%EC%9E%88%EB%8A%94%20n%EA%B0%9C%EC%9D%98%20%EC%88%AB%EC%9E%90.cpp)
+ ```vector``` 클래스의 주요한 method -> vector 클래스는 python의 list와 같은 배열 형태
  + ```push_back()```: vector의 끝에 새로운 원소를 추가
  + ```pop_back()```: vector의 끝에서 원소를 제거
  + ```size()```: vector에 포함된 원소의 개수를 반환
  + ```empty()```: vector가 비어있는지 확인
  + ```clear()```: vector의 모든 원소를 제거
  + ```erase()```: vector에서 원소를 제거
    + ```arr.erase(unique(arr.begin(), arr.end()), arr.end());``` -> C++에서 중복된 요소를 제거하기 위한 흔히 사용되는 패턴 
  + ```begin()```: vector의 첫 번째 원소를 가리키는 반복자를 반환
  + ```end()```: vector의 마지막 원소 다음을 가리키는 반복자를 반환
  + ```at()```: 인덱스를 이용하여 vector의 원소에 접근
+ **C++** 에서는 ```if / for / while```문 뒤에 ```()```로 조건을 표시


#### [문자열 내 p와 y의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/12916)
+ 제출단안 : [문자열 내 p와 y의 개수.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%82%B4%20p%EC%99%80%20y%EC%9D%98%20%EA%B0%9C%EC%88%98.cpp)
+ ```and / or```은 **C++** 에서는 ```&& / ||``` 로 표현한다.
+ ```if / else if```는 ```{}```로 각각 묶어 가독성과 수정 편리성을 높인다.


#### [정수 제곱근 판별](https://school.programmers.co.kr/learn/courses/30/lessons/12934)
+ 제출답안 : [정수 제곱근 판별.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/%EC%A0%95%EC%88%98%20%EC%A0%9C%EA%B3%B1%EA%B7%BC%20%ED%8C%90%EB%B3%84.cpp)
+ ```#include <cmath>```헤더 파일 통해서 계산 시간을 줄일 수 있다.
  + ```sqrt(x)```: x의 제곱근을 반환
  + ```pow(x, y)```: x의 y 거듭제곱을 반환
  + ```sin(x)```: x의 사인 값을 반환 (x는 라디안)
  + ```cos(x)```: x의 코사인 값을 반환 (x는 라디안)
  + ```tan(x)```: x의 탄젠트 값을 반환 (x는 라디안)
  + ```log(x)```: x의 자연로그 값을 반환
  + ```exp(x)```: e의 x 거듭제곱을 반환


#### [문자열을 정수로 바꾸기](https://school.programmers.co.kr/learn/courses/30/lessons/12925?language=cpp)
+ 제출답안 : [문자열을 정수로 바꾸기.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%84%20%EC%A0%95%EC%88%98%EB%A1%9C%20%EB%B0%94%EA%BE%B8%EA%B8%B0.cpp)
+ 자료형을 변형해주는 함수는 다양하다.
  + ```stod```: ```string```을 ```double``` 형태로 변환하는 함수 ```<string>``` 헤더 파일에 선언
    + 예시: double num = stod("1.23");
  + ```stof```: ```string```을 ```float``` 형태로 변환하는 함수 ```<string>``` 헤더 파일에 선언
    + 예시: float num = stof("1.23");
  + ```stoi```: ```string```을 ```int``` 형태로 변환하는 함수 ```<string>``` 헤더 파일에 선언
    + 예시: int num = stoi("123");
  + ```to_string()```: ```int```를 ```string```자료형으로 변환
    + 예시: str += to_string(int)


#### [콜라츠 추측](https://school.programmers.co.kr/learn/courses/30/lessons/12943?language=cpp)
+ 제출답안 : [콜라츠 추측.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/%EC%BD%9C%EB%9D%BC%EC%B8%A0%20%EC%B6%94%EC%B8%A1.cpp)
+ **삼항 연산자**의 구성 ```(condition) ? (value_if_true) : (value_if_false)```
  + condition은 조건을 나타내는 표현식, 이 값이 참(true)이면 value_if_true가 반환, 거짓(false)이면 value_if_false가 반환


#### [나누어 떨어지는 숫자 배열](https://school.programmers.co.kr/learn/courses/30/lessons/12910?language=cpp)
+ 제출답안 : [나누어 떨어지는 숫자 배열.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/%EB%82%98%EB%88%84%EC%96%B4%20%EB%96%A8%EC%96%B4%EC%A7%80%EB%8A%94%20%EC%88%AB%EC%9E%90%20%EB%B0%B0%EC%97%B4.cpp)
+ ```#include <algorithm>```의 key method
  + ```sort()```: 벡터나 배열 등의 컨테이너를 정렬 (오름차순으로)
    + cf) ```sort(arr.rbegin(), arr.rend());``` => 내림차순으로 정렬
  + ```min()```: 두 값 중에서 작은 값을 반환
    + ```min_element(array.begin(),array.end())```: array에서 가장 작은 값을 반환 
  + ```max()```: 두 값 중에서 큰 값을 반환
  + ```find()```: 주어진 값이 컨테이너에 있는지 검사하고, 해당 값을 가진 원소의 iterator를 반환
  + ```reverse()```: 벡터나 배열 등의 컨테이너를 역순으로 뒤집는다
  + ```lower_bound()```: 정렬된 컨테이너에서 특정 값을 찾고, 해당 값을 가진 원소의 iterator를 반환, 만약 해당 값이 없으면, 그 값보다 크거나 같은 값 중에서 가장 작은 값을 가진 iterator를 반환
  + ```upper_bound()```: lower_bound()와 비슷하지만, 해당 값을 가진 원소가 아니라, 그 값보다 큰 값을 가진 iterator를 반환

#### [가운데 글자 가져오기](https://school.programmers.co.kr/learn/courses/30/lessons/12903?language=cpp)
+ 제출답안 : [가운데 글자 가져오기.cpp](https://github.com/kxxbeomjun/Algorithm-study/blob/main/programmers/Level%201/%EA%B0%80%EC%9A%B4%EB%8D%B0%20%EA%B8%80%EC%9E%90%20%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0.cpp)
+ C++에서는 string index 접근가능하다.
  + 추가로 ```str.substr(a,b)```통해 string을 slicing 할 수 있다. ```a```는 **시작 index 위치**, ```b```는 **추출할 문자열의 길이**
+ C++에서 정수 나눗셈은 **나머지를 버린다.** ex) ```5/2 = 2```


  
