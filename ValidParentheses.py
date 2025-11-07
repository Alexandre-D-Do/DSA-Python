class Solution:
    def isValid(self, s: str) -> bool:
        slen = len(s)
        for i, char in enumerate(s) :
            
            if (i % 2) == 0 :
                # Check if this is the last character
                if i == (slen - 1) :
                    return False
                elif s[i: i+1] == "(" :
                    if s[i+1: i+1] != ")" :
                        return False
                elif s[i: i+1] == "[" :
                    if s[i+1: i+1] != "]" :
                        return False
                elif s[i: i+1] == "{" :
                    if s[i+1: i+1] != "}" :
                        return False
                else :
                    return False
        return True


''''''