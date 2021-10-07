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

    
    
# substring 하나씩 해서 그 string에 각각 char가 2개 이상인지 조사(1개 인지) 1개일때만 저장해서 길이비교
# 혹은 char 2개 이상인 앧ㄹ 찾아서 그 애들 거리(int)가 가장 먼 애 그 int return (simple)
# but, 이렇게 하면 acedae 이렇게 aa 중간에 아무것도 없는 애들은 바로 찾을 수 있지만
# aceddae 이렇게 중간에 dd 똑같은거 있으면 안됨. 그럼 가장 먼 애 찾아도 중간에 중복되는애 있으니까 안됨
# 딕셔너리에 같은 문자인 애들 index를 짝지어 줘서 하는 방법. -> 이건 같은게 3개면 망함.
