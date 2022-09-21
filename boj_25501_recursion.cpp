#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;

	for (int t = 0; t < T; t++)
	{
		string s;
		cin >> s;

		int cnt = 0;
		int left = 0;
		int right = s.length() - 1;
		int flag = 1;
		for (; left <= right; left++, right--)
		{
			cnt++;
			if (s[left] != s[right])
			{
				flag = 0;
				break;
			}
		}

		cout << flag << " " << (flag && s.length() % 2 == 0 ? cnt + 1 : cnt) << "\n";
	}

	return 0;
}