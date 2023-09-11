import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1 = Employee("Fname", "Lname" , 100)
    
    def tearDown(self) -> None:
        del self.emp1

    def test_firstName(self):
        expected = "Fname"
        self.assertEqual(self.emp1.first, expected)

    def test_mail(self):
        expected = "fname.lname@gmail.com"
        self.assertEqual(self.emp1.email(), expected)

    def test_raise_salary(self):
        expected = 105.0
        self.assertAlmostEqual(self.emp1.applay_rise(), expected)


if __name__ == "__main__":
    unittest.main()
