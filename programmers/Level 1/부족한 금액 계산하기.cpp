#include <iostream>

using namespace std;

long long solution(int price, int money, int count)
{
    long long answer;
    long long total_price = 0;
    
    for(int i = 1 ; i <= count ; i++){
        total_price += i*price;
    }
    if(money - total_price < 0){
        answer = total_price - money;
    }
    else{
        answer = 0;
    }
    
    return answer;
}