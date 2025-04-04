class Solution(object):
    def myPow(self, x, n):
        p=1.00
        if(n<0):
            w=1.00
            for i in range(0,n,-1):
                w=w*x
            r=1/w
            return (r)
        elif(n==0):
            return 1
        else:
             for i in range(n):
                 p*=x    
             return p    
