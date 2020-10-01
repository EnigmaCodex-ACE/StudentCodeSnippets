# Medium
# https://leetcode.com/problems/longest-common-subsequence/

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text2)
        n = len(text1) 
        d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1): 
                if i == 0 or j == 0:
                    d[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    d[i][j] = d[i-1][j-1] + 1
                else:
                    d[i][j] = max(d[i-1][j], d[i][j-1])
        return d[n][m]