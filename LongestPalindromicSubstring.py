#The runtime complexity of this solution is O(N^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        start = 0
        end = 0

        for i in range(size):
            for j in range(2):
                left = i
                right = i + j
                while left >=0 and right + 1 <= size and s[left] == s[right]:
                    left -= 1
                    right += 1
                left += 1
                right -= 1
                if (right - left) > (end - start):
                    end = right
                    start = left
                    
        return s[start: end + 1]

'''
Given a string s, return the longest

in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

'''
