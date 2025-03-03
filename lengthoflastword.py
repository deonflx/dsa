class Solution:
    def lengthOfLastWord(self, s):
       
        words = s.strip().split()
        

        if not words:
            return 0
            
        
        return len(words[-1])


    
        
        test_str = "my name is deon"
        result = solution.lengthOfLastWord(test_str)
        