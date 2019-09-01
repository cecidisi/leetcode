
# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.


def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        
        def is_sqrt(num):
            return True if num*num <= x and (num+1)*(num+1)> x else False
                        
        l = 0
        h = int(x/2)
        
        while True:
            m = int((h+l)/2)
            # print("l = %d, m = %d, h = %d" %(l,m,h))
            if is_sqrt(l): return l
            if is_sqrt(m): return m
            if is_sqrt(h): return h
            if m**2 > x:
                h = m-1
            else:
                l = m+1
    
