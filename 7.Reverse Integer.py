class Solution:
    def reverse(self, x: int) -> int:
        if x>=int(2**31) or x<=0-int(2**31):
            z=0
        else:
            y = str(x)
            z = ''
            if y[0] == '-':
                z=z+'-'
                for i in range(len(y)-1,0,-1):
                    z=z+y[i]
            else:
                for i in reversed(range(len(y))):
                    z=z+y[i]
        z=int(z)
        if z>=int(2**31) or z<=0-int(2**31):
            z=0
        return z
