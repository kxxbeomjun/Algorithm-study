#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    int tmp = budget;
    
    sort(d.begin(), d.end());
    
    for(int i = 0 ; i<d.size(); i++){
        if (tmp >= d[i]){
            tmp -= d[i];
            answer += 1;
        }
        else{
            break;
        }
    }
    
    return answer;
}