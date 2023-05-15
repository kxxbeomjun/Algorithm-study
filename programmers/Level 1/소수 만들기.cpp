#include <vector>
#include <iostream>
using namespace std;

int solution(vector<int> nums) {
    int answer = 0;
    
    for(int i=0; i<nums.size()-2; i++){
        for(int j=i+1; j<nums.size()-1; j++){
            for(int k=j+1; k<nums.size(); k++){
                int tmp;
                tmp = nums[i] + nums[j] + nums[k];
                bool prime = true;
                for (int m=2; m*m <= tmp; m++){
                    if (tmp % m ==0){
                        prime = false;
                        break;
                    }
                }
                if (prime == true){
                    answer += 1;
                }
            }
        } 
    }

    return answer;
}