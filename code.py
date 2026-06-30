class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u=0
        d=0
        l=0
        r=0
        for move in moves:
            if move=="U":
                u+=1
                
            if move=="D":
                d+=1
                
            if move=="L":
                l+=1
                
            if move=="R":
                r+=1
                
        n=(l-r)
        i=(u-d)
        if n == 0 and i==0:
            return True
        return False
        
