#include <string>
#include <vector>

using namespace std;

vector<int> solution(long long n) {
    vector<int> answer;
    
    while true{
        answer.push_back(n%10); #1의 자리수 가지고 오기
        n = n/10; #1의 자리수 버리기
        if (n == 0){
            break;
        }
    }
    
    return answer;
}