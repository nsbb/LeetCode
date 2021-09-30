class Solution:
    def romanToInt(self, s: str) -> int:
        result=0
        s=s.replace('IV','1')
        s=s.replace('IX','2')
        s=s.replace('XL','3')
        s=s.replace('XC','4')
        s=s.replace('CD','5')
        s=s.replace('CM','6')
        for i in s:
            if i == 'M':
                result+=1000
            elif i == '6':
                result+=900
            elif i == 'D':
                result+=500
            elif i == '5':
                result+=400
            elif i == 'C':
                result+=100
            elif i == '4':
                result+=90
            elif i == 'L':
                result+=50
            elif i == '3':
                result+=40
            elif i == 'X':
                result+=10
            elif i == '2':
                result+=9
            elif i == 'V':
                result+=5
            elif i == '1':
                result+=4
            elif i == 'I':
                result+=1
        return result
