from django.test import TestCase
from calc import add, subt

class Calctest(TestCase):
    def test_add_nm(self):
        self.assertEqual(add(3,4), 7)

    def test_sub_num(self):
        self.assertEqual(subt(5,0), 5)


