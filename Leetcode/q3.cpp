#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int index[256];
        fill(begin(index), end(index), -1);

        int maxLen = 0, start = 0;
        for (int end = 0; end < (int)s.size(); ++end) {
            unsigned char c = s[end];
            if (index[c] >= start)
                start = index[c] + 1;
            index[c] = end;
            maxLen = max(maxLen, end - start + 1);
        }
        return maxLen;
    }
};
