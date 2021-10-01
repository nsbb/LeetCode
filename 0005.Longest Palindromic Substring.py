class Solution:
    def longestPalindrome(self, s: str) -> str:
        count=0;result=s
        while s:
            for i in range(count+1):
                result=s[i:len(s)-count+i]
                if result == result[::-1]:
                    return result
            count+=1
