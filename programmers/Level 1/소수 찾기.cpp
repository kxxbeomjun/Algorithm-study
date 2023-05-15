#include <string>
#include <vector>
 
using namespace std;
 
int solution(int n) {
    int answer = 0;
    vector<bool> v(n+1, true);
    
    for(int i = 2; i <= n; i++)
    {
        if(v[i] == true)
        {
            for(int j = 2; j*i <= n; j++)
            {
                v[j*i] = false;
            }    
            answer++;
        }
        
    }
    
    return answer;
}