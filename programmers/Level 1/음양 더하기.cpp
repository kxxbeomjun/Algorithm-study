#include <string>
#include <vector>

using namespace std;

int solution(vector<int> absolutes, vector<bool> signs) {
    int answer = 0;
    
    for(int i=0; i<signs.size(); i++){
        if (signs[i] == true){
            absolutes[i] = absolutes[i];
        }
        else{
            absolutes[i] = - absolutes[i];
        }
    }
    for(int j=0; j<absolutes.size(); j++){
        answer += absolutes[j];
    }
    
    
    return answer;
}