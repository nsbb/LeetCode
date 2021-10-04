class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) == 1 or len(strs[0])==0:
            return strs[0]
        length=len(strs[0])
        for i in strs:
            if length>len(i):
                length=len(i)
        for i in range(length):
            count = 1
            for j in range(1,len(strs)):
                if strs[0][i] == strs[j][i]:
                    count+=1
                else:
                    return result
                if count == len(strs):
                    result+=strs[0][i]

#터미널에서 하면 ['ab','a'] 인풋 주면 'a'로 제대로 return 하는데 leetcode에서 돌리면 계속 null return 함. 이유를 모르겠음.
