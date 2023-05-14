#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int left, int right) {
    int answer = 0;
    
    for(int i = left; i<=right; i++){
        int root = sqrt(i);
        if(root * root == i){
            answer -= i;
        }
        else{
            answer += i;
        }
    }
    
    return answer;
}