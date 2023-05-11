#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 1;
    
    while(answer<n){
        if (n%answer == 1)
            break;
        else
            answer += 1;
    }
    return answer;
}