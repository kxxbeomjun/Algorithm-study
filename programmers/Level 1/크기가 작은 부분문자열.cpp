#include <string>
#include <vector>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    
    for(int i = 0; i<t.size()-p.size()+1; i++){
        //array를 p의 길이만큼 slicing
        string t_tmp = t.substr(i, p.size());
        //두 값을 비교 : str -> int로 type 변환
        if (stol(t_tmp) <= stol(p)){
            answer += 1;
        }
        
    }
    
    return answer;
}