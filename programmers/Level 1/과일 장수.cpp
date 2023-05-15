#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, int m, vector<int> score) {
    int answer = 0;
    
    //내림차순으로 정렬
    sort(score.rbegin(), score.rend());
    
    //for문을 만들 수 있는 개수인 m으로 나눈 수까지만 loop 실행
    for(int i=0; i<score.size()/m; i++){
        //임시로 m개씩 끊어서 새로운 vector class 형성
        vector<int> tmp(score.begin()+(i*m), score.begin()+((i+1)*m));
        //이미 내림차순으로 정렬되어 있으므로 마지막 원소 * m = 가격
        answer += tmp[tmp.size()-1]*m;
    }
    
    
    return answer;
}