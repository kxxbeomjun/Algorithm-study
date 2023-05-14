#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    
    for(int i=0; i<numbers.size()-1; i++){
        for(int j=i+1; j<numbers.size(); j++){
            //서로 다른 인덱스의 두 값을 더한 값
            int sum = numbers[i] + numbers[j];
            //answer array에 없는 값이면 push_back
            if (find(answer.begin(), answer.end(),sum) == answer.end()){
                answer.push_back(sum);
            }
        }
    }
    sort(answer.begin(), answer.end());
    return answer;
}