# 11.3 Employee

class Employee():
    """Информация о работнике."""

    def __init__(self, name, last_name, annual_salary):
        """Сохраняет данные о работнике."""
        self.name = name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self):
        """По умолчанию прибавляет $5000 к ежегодному окладу."""
        self.annual_salary += 5000

    def custom_give_raise(self, custom_salary):
        """Прибавляет любую другую сумму к ежегодному окладу."""
        self.annual_salary += custom_salary


