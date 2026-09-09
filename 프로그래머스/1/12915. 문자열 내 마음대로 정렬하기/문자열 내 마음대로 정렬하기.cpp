#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
    // key : n번째 글자 value : string
    map<char, set<string>> mp;
    for(int idx = 0; idx < strings.size(); ++idx)
    {
        auto& str = strings[idx];
        mp[str[n]].insert(strings[idx]);
    }
    
    auto iter = mp.begin();
    auto iterEnd = mp.end();
    for(; iter != iterEnd; ++iter)
    {
        for(auto& str : iter->second)
        {
            answer.push_back(str);
        }
    }
    
    return answer;
}