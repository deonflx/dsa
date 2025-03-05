class Solution(object):
    def plusOne(self, digits):
        if digits[-1]==9:
           digits.pop()
           digits.append(1)
           digits.append(0)
        else:
            digits[-1]=(digits[-1]+1)   

        return digits
    print(plusOne(" ",[9]) )   