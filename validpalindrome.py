class Solution(object):
    def isPalindrome(self, s):
        
        arr=""
        for i in s:
            if i.isalnum():
               arr=arr+i 
               print(i) 
        arr=arr.lower()
        print(arr)

        if(arr==arr[::-1]):
                return True
        return False  
    print(isPalindrome(1,"A man, a plan, a canal: Panama"))
