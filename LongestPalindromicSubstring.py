class Solution:
    def longestPalindrome(self, s: str) -> str:
        reverseds = s[::-1]
        slength = len(s) 
        longestlength = 1
        longestsub = s[0]
        # Check if s is a palindrome
        if s == reverseds or slength == 1:
            return s
        for i, char in enumerate(s):
            slength = len(s)
            if i == (len(s) - 1):
                break
            substring = s[i:]
            reversedsub = substring[::-1]
            if substring == reversedsub and len(substring) > longestlength:
                    longestlength = len(substring)
                    longestsub = substring
            while slength > i:
                substring = s[i : slength - 1]
                reversedsub = substring[::-1]
                if substring == reversedsub and len(substring) > longestlength:
                    longestlength = len(substring)
                    longestsub = substring
                slength -= 1 
        return longestsub