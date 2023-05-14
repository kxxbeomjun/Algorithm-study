#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;

    for (int i = 0; i < arr.size(); i++) {
        if (i == 0 || arr[i] != arr[i - 1]) {
            //이전 항과 다른 숫자일 경우만 push_back, 나머지는 통과
            answer.push_back(arr[i]);
        }
    }

    return answer;
}