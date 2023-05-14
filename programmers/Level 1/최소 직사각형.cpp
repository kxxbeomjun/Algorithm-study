#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int max_width = 0;  // 가장 긴 가로 길이
    int max_height = 0; // 가장 긴 세로 길이

    for (const vector<int>& card : sizes) {
        max_width = max(max_width, max(card[0], card[1]));
        max_height = max(max_height, min(card[0], card[1]));
    }

    int answer = max_width * max_height;

    return answer;
}