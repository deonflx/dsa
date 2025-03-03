class Solution(object):
    def lengthOfLastWord(self, s):
         last=s.strip().split()
         print(len(last[-1]))
         return len(last[-1])

        