import pytest
import answer

class TestAnswer():
    __correct__ = 0
    __total__ = 0

    @classmethod
    def setup_class(cls):
        print("Before")
        cls.__correct__ = 0
        cls.__total__ = 0

    @classmethod
    def teardown_class(cls):
        print(f"Score:{(cls.__correct__ / cls.__total__) * 100}%")

    def test_Q1_Rectangel_1_area(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(3,4)
        result = x.area()
        assert (result == 12)
        TestAnswer.__correct__ += 1

    def test_Q1_Rectangel_1_perimeter(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(3,4)
        result = x.perimeter()
        assert (result == 14)
        TestAnswer.__correct__ += 1

    def test_Q1_Rectangel_1_diagonal(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(3,4)
        result = x.diagonal()
        assert (round(result,2) == 5.0)
        TestAnswer.__correct__ += 1

    def test_Q1_Rectangel_1_diagonal(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(3,4)
        result = x.is_square()
        assert (result == False)
        TestAnswer.__correct__ += 1

    def test_Q1_Rectangel_1_diagonal(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(3,4)
        x.resize(5,10)
        result = x.area()
        assert (result == 50)
        TestAnswer.__correct__ += 1

    def test_Q1_Rectangel_2_area(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(10,10)
        result = x.area()
        assert (result == 100)
        TestAnswer.__correct__ += 1

    def test_Q1_Rectangel_2_area(self):
        TestAnswer.__total__ += 1
        x = answer.Rectangle(10,10)
        result = x.is_square()
        assert (result == True)
        TestAnswer.__correct__ += 1

    def test_Q2_normal_1(self):
        TestAnswer.__total__ += 1
        s = "egg"
        t = "add"
        result = answer.isIsomorphic(s,t)
        assert (result == True)
        TestAnswer.__correct__ += 1

    def test_Q2_normal_2(self):
        TestAnswer.__total__ += 1
        s = "foo"
        t = "bar"
        result = answer.isIsomorphic(s,t)
        assert (result == False)
        TestAnswer.__correct__ += 1

    def test_Q2_normal_3(self):
        TestAnswer.__total__ += 1
        s = "paper"
        t = "title"
        result = answer.isIsomorphic(s,t)
        assert (result == True)
        TestAnswer.__correct__ += 1


    def test_Q2_normal_4(self):
        TestAnswer.__total__ += 1
        s = "papapaper"
        t = "titititle"
        result = answer.isIsomorphic(s,t)
        assert (result == True)
        TestAnswer.__correct__ += 1


    def test_Q3_normal_1(self):
        TestAnswer.__total__ += 1
        arr = [2,2,3,4]
        result = answer.findLucky(arr)
        assert (result == 2)
        TestAnswer.__correct__ += 1

    def test_Q3_normal_2(self):
        TestAnswer.__total__ += 1
        arr = [1,2,2,3,3,3]
        result = answer.findLucky(arr)
        assert (result == 3)
        TestAnswer.__correct__ += 1

    def test_Q3_normal_3(self):
        TestAnswer.__total__ += 1
        arr = [2,2,2,3,3]
        result = answer.findLucky(arr)
        assert (result == -1)
        TestAnswer.__correct__ += 1

    def test_Q3_normal_4(self):
        TestAnswer.__total__ += 1
        arr = [5]
        result = answer.findLucky(arr)
        assert (result == -1)
        TestAnswer.__correct__ += 1
    
    def test_Q3_normal_5(self):
        TestAnswer.__total__ += 1
        arr = [7,7,7,7,7,7,7]
        result = answer.findLucky(arr)
        assert (result == 7)
        TestAnswer.__correct__ += 1

    def test_Q4_normal_1(self):
        TestAnswer.__total__ += 1
        nums = [12,345,2,6,7896]
        result = answer.findNumbers(nums)
        assert (result == 2)
        TestAnswer.__correct__ += 1

    def test_Q4_normal_2(self):
        TestAnswer.__total__ += 1
        nums = [555,901,482,1771]
        result = answer.findNumbers(nums)
        assert (result == 1)
        TestAnswer.__correct__ += 1

    def test_Q4_normal_3(self):
        TestAnswer.__total__ += 1
        nums = [5464,545,12131,15454,112,1,65,457]
        result = answer.findNumbers(nums)
        assert (result == 2)
        TestAnswer.__correct__ += 1
