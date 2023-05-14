#include <string>
#include <vector>
#include <algorithm>
 
using namespace std;
 
int k;
bool cmp (string a, string b) {
    if (a[k] != b[k]) return a[k] < b[k];
    else return a < b;
}
 
vector<string> solution(vector<string> strings, int n) {
    k = n;
    sort(strings.begin(), strings.end(), cmp);
    return strings;
}
