class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:  
            return 0
        a=x/2
        while True:
            y= (a+(x/a))/2
            if y==a:
                break
            a=y
        return int(a)