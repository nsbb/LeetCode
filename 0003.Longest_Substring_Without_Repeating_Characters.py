class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in range(len(s)):
            if s[i:].count(s[i]) >=2:
                for j in range(i,len(s)):
                    ind=s[j:].find(s[i])
                    #ind=s.find(s[i],j)
                    if ind >= 0:
                        ind+=j

def main():
    s = Solution()

if __name__ == "__main__":
    main()

    
    
# substring 하나씩 해서 그 string에 각각 char가 2개 이상인지 조사(1개 인지) 1개일때만 저자애서 길이비교
# 혹은 char 2개 이상인 앧ㄹ 찾아서 그 애들 거리(int)가 가장 먼 애 그 int return( simple)
