import string;
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        str=string(n)
        n=str[::-1]
        return (int(n))
    print(reverseBits(1,110)) # 964176192