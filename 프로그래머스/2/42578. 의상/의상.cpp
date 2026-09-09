#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string, int> mp;
    for(auto& item : clothes)
    {
        auto& name = item[0];
        auto& kind = item[1];
        mp[kind]++;
    }
    
    auto iter = mp.begin();
    auto iterEnd = mp.end();
    for(; iter != iterEnd; ++iter)
    {
        answer *= iter->second + 1;
    }
    answer--;
    
    return answer;
}