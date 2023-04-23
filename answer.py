
"""
Questons 1:
========================================================================================================
Given an OOP program that is about rectangle, please follow the requests above every function.
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #This area function is used to return the area of a rectangle, use the rectangle function that area = width * height.
    #Example: area for a rectangle(3,4) will be 3 * 4 = 12.
    def area(self):
        return 
    #This perimeter function is used to return the perimeter of a rectangle.
    #Example: preimeter for a rectangle(3,4) will be (3+4) * 2 = 14.
    def perimeter(self):
        return 
    #This diagonal function is used to compute the length of the diagonal of the rectangle using the Pythagorean theorem.
    #Example: diagonal for a rectangle(3,4) will be square(3^2 + 4^2) = 5
    def diagonal(self):
        return 
    #This is_square function is used to check if this rectangle is square, if this rectangle is square, return True, otherwise return False.
    #Checks if the rectangle is a square (i.e., if its width and height are equal).
    #Example: is_square for a rectangle(3,4) will be False
    #Example: is_square for a rectangle(4,4) will be True
    def is_square(self):
        return 
    #This resize function is used to resize the rectangle. New_width and new_height are the new width and height.
    def resize(self, new_width, new_height):
        self.width = 
        self.height = 

"""
Questons 2:
========================================================================================================
Given two strings s and t, determine whether they are isomorphic.
If the characters in s can be replaced according to some mapping relationship to get t, then the two strings are isomorphic.
Each occurrence of a character should map to another character without changing the order of the characters. 
Different characters cannot be mapped to the same character, the same character can only be mapped to the same character, and a character can be mapped to itself.
Example 1:
========================================
Input: s = "egg", t = "add"
Output: true
Example 2:
========================================
Input: s = "foo", t = "bar"
Output: false
Example 3:
========================================
Input: s = "paper", t = "title"
Output: true
"""
def isIsomorphic(s, t):
    #write your code here, return True or False
    return 

"""
Questons 3:
========================================================================================================
Given an integer array arr, please judge whether there are three consecutive elements in the array that are all odd numbers: if yes, please return true; otherwise, return false.
Example 1:
========================================
Input: arr = [2,2,3,4]
Output: 2
Explanation:The only lucky number in the array is 2 , because the value 2 occurs 2 times as well.
Example 2:
========================================
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation:1, 2, and 3 are all lucky numbers, and only the largest 3 among them needs to be returned.
Example 3:
========================================
Input: arr = [2,2,2,3,3]
Output: -1
Explanation:There are no lucky numbers in the array.
Example 4:
========================================
Input: arr = [5]
Output: -1
Example 5:
========================================
Input: arr = [7,7,7,7,7,7,7]
Output: 7
"""
def findLucky(arr):

    return ans

"""
Questons 4:
========================================================================================================
Given an integer array nums, please return the number of numbers whose median is even.
Example 1:
========================================
Input: nums = [12,345,2,6,7896]
Output: 3
Explanation:
12 is 2 digits (even number of digits)
345 is 3 digits (odd number of digits)
2 is 1 digit (odd number of digits)
6 is 1 digit (the number of digits is odd)
7896 is 4 digits (even number of digits)
So only 12 and 7896 are numbers with an even number of digits
Example 2:
========================================
Input: nums = [555,901,482,1771]
Output: 1
Explanation:Only 1771 is a number with an even number of digits.
Example 3:
========================================
Input: nums = [5464,545,12131,15454,112,1,65,457]
Output: 2
Explanation:
Only 5464 and 65 are numbers with an even number of digits.
"""
def findNumbers(nums):

    return ans