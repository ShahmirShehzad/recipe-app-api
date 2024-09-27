#sample tests

from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    #test calc module
    def test_add_nums(self):
        res = calc.add(5,6)
        self.assertEqual(res,11)

    def test_sub_nums(self):
        res = calc.subtract(10,15)
        self.assertEqual(res,5)