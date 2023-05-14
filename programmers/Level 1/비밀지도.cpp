#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    
    for(int i = 0; i < n; i++)
    {   
        //for 문이 5번 반복하는데, 각 줄에서 초기화된 tmp를 사용
        string tmp = "";
        
        // |(or) 비트 연산자를 이용해서 이진법으로 변경 ex) 101 + 011 = 111 
        arr1[i] = arr1[i] | arr2[i];
        
        while(tmp.size() != n)
        {   
            if(arr1[i] % 2 == 0)
                tmp.push_back(' ');
            else
                tmp.push_back('#');
            arr1[i] /= 2;
        }
        
        //tmp를 역순으로 정렬 위에서 push_back할 때 역순으로 정렬된다.
        reverse(tmp.begin(), tmp.end());
        answer.push_back(tmp);
    }
    return answer;
}