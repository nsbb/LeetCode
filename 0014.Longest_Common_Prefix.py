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
