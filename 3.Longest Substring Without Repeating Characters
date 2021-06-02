class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=[]
        length=len(s)
        if length == 0:
            return 0
        elif length == 1:
            return 1
        else:
            first=s[0]
            sub=first
            for i in s[1:]:
                if first is not i and i not in sub:
                    sub+=i
                    first=i
            return len(sub)

def main():
    s = Solution()

if __name__ == "__main__":
    main()
