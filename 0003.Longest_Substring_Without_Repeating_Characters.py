class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in range(len(s)):
            if s[i:].count(s[i]) >=2:
                for j in range(i,len(s)):
                    ind=s[j:].find(s[i])
                    if ind >= 0:
                        ind+=j

def main():
    s = Solution()

if __name__ == "__main__":
    main()
