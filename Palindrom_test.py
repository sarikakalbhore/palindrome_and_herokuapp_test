def reverseString(text): 
    return text[::-1] 
  
def isPalindrome(text): 
    # Checking if both strings are equal or not 
    if (text == reverseString(text)): 
        return True
    return False
  

###############################################
import unittest

class TestSum(unittest.TestCase):

    def test_Palindrome_Success(self):
        # 1 represents True 
        self.assertEqual(isPalindrome("KannaK"), 1, "Should be a Palindrome")

    def test_Palindrome_Fail(self):
        # 0 represents False 
        self.assertEqual(isPalindrome("KanbaK"), 0, "Should not be a Palindrome")

if __name__ == '__main__':
    unittest.main()

