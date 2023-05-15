#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int k, vector<int> score) {
    vector<int> answer;
    vector<int> tmp;
    
    for(int i = 0; i<score.size(); i++){
        tmp.push_back(score[i]);
        sort(tmp.begin(), tmp.end());
        
        //아래 if.else문을 다음과 같이 변형 가능
        // i < k ? answer.push_back(*min_element(temp.begin(), temp.end())) : answer.push_back(temp[temp.size() - k]);
        if (i<k){
            answer.push_back(*min_element(tmp.begin(), tmp.end()));
        }
        else{
            answer.push_back(tmp[tmp.size()-k]);
        }
        
    }
    
    
    
    return answer;
}