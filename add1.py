class Solution(object):
    def plusOne(self, digits):
        
        if not digits:
            return [1]
            
        
        digits = list(digits)
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
        
       
        return [1] + digits


    # Create instance
    solution = Solution()
    
    # Test cases
    test_cases = [
        [9, 9],
        [1, 2, 3],
        [9],
        [9, 9, 9],
        [1,9,9,9]
    ]
    
    # Run tests
    for test in test_cases:
        result = solution.plusOne(test)
        print(f"Input: {test} -> Output: {result}")

