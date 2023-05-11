#include <string>
#include <vector>

using namespace std;

vector<long long> solution(int x, int n) {
    vector<long long> answer;
    
    for (int y=1; y<n+1; y++){
        answer.push_back(x*y);
    }
    
    return answer;
}