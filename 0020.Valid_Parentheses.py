class Solution:
    def isValid(self, s: str) -> bool:
        dic={')':'(','}':'{',']':'['}
        stack=[]
        count = 0
        if len(s)%2 ==1:
            return False
        for i in s:
            if i not in dic:
                stack.append(i)
                count+=1
            else:
                if count == 0:
                    return False
                else:
                    if stack.pop() != dic[i]:
                        return False
                    count-=1
        if len(stack) != 0:
            return False
        return True
