class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
            count = 1
            for j in range(1,len(strs)):
                if strs[0][i] == strs[j][i]:
                    count+=1
                else:
                    return result
                if count == len(strs):
                    result+=strs[0][i]
