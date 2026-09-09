#include <vector>
#include <map>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    int count = nums.size() / 2;
    // key : 폰켓몬 종류 번호 value : 개수
    map<int, int> mp;
    for(auto& pokemon : nums) mp[pokemon]++;
    if(mp.size() > count)
    {
        answer = count;
    }
    else
    {
        answer = mp.size();
    }
    
    return answer;
}