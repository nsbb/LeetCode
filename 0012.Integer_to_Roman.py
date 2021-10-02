class Solution:
    def intToRoman(self, num: int) -> str:
        s=''
        while num:
            if num>=1000:
                s+='M'
                num-=1000
            else:
                if num>=900:
                    s+='CM'
                    num-=900
                elif num>=500:
                    s+='D'
                    num-=500
                elif num>=400:
                    s+='CD'
                    num-=400
                elif num>=100:
                    s+='C'
                    num-=100
                else:
                    if num>=90:
                        s+='XC'
                        num-=90
                    elif num>=50:
                        s+='L'
                        num-=50
                    elif num>=40:
                        s+='XL'
                        num-=40
                    elif num>=10:
                        s+='X'
                        num-=10
                    else:
                        if num>=9:
                            s+='IX'
                            num-=9
                        elif num>=5:
                            s+='V'
                            num-=5
                        elif num>=4:
                            s+='IV'
                            num-=4
                        elif num>=1:
                            s+='I'
                            num-=1
        return s
