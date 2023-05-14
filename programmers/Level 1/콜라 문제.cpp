#include <string>
#include <vector>

using namespace std;

int solution(int a, int b, int n) {
    int answer=0;
    
    //무한 루프 돌리게 한다음에 break 구문
    while(1){
        if(n<a) break;
        answer+=((n/a)*b);
        n=(n/a)*b+n%a;
    }
    
    return answer;
}