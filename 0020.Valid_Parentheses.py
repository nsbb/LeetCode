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

    
#스택 말고 계속 다음걸로 넘어가면서 dic의 key value 비교해서 맞으면 count+1해서 count가 len(s)/2면 true 아니면 false 하는 방법
