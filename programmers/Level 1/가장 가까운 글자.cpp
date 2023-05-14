#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    
    //맨 처음은 어짜피 -1
    answer.push_back(-1);
    
    //두번째부터 따지기
    for(int i=1; i<s.size(); i++){
        vector<int> tmp;
        
        for(int j=0; j < i; j++){
            if (s[i] == s[j]){
                tmp.push_back(i-j);
            }
        }    
        if (tmp.size() == 0){
            answer.push_back(-1);
        }
        else{
            answer.push_back(*min_element(tmp.begin(), tmp.end()));
        }         
    }
    
    return answer;
}