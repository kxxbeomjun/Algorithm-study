#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<int> digit_3;
    
    while (n != 0){
        digit_3.push_back(n%3);
        n = n/3;
    }
    
    int mul = 1;
    for(int i = digit_3.size()-1 ; i >= 0 ; i--){
        answer += mul * digit_3[i];
        mul = mul * 3;
    }
    
    return answer;
}