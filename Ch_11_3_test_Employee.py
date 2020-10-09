import unittest
from Ch_11_3_Employee import Employee


class TestEmployee(unittest.TestCase):
    """Информация о работнике."""

    def setUp(self):
        """Создание всей необходимой информации о сотруднике для всех тестовых методов."""

        name = 'Leha'
        last_name = 'Lykov'
        annual_salary = 500
        self.my_employee = Employee(name, last_name, annual_salary)

    def test_give_default_raise(self):
        """Проверяет, что по умолчанию прибавляется $5000 к ежегодному окладу."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 5500)

    def test_give_custom_raise(self):
        """Проверяет, что прибавляется любая другая сумма к ежегодному окладу."""
        self.my_employee.custom_give_raise(1000)
        self.assertEqual(self.my_employee.annual_salary, 1500)


if __name__ == '__main__':
    unittest.main()
