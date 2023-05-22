import unittest

from hw_18 import MyStr, User


# Task 48.1
class UnitTests(unittest.TestCase):
    def setUp(self):
        self.user_1 = User('Testname')
        self.user_2 = User('TESTNAME')
        self.name_lower_case = MyStr('testname')

    def test_user(self):
        self.assertIs(type(self.user_1.name), str)
        self.assertEqual(self.user_1, self.user_2)

    def test_str(self):
        self.assertEqual(str(self.name_lower_case), 'TESTNAME')


if __name__ == '__main__':
    unittest.main()
