# Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
#       ○ шестизначный идентификационный номер
#       ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

from Task03 import Human


class Employee(Human):
    def __init__(self, employee_id: int, *args, **kwargs):
        self.employee_id = employee_id
        super().__init__(*args, **kwargs)

    def get_level(self):
        return sum((int(i) for i in str(self.employee_id))) % 7


if __name__ == '__main__':
    e1 = Employee(145858, 'Алексей', 'Валерьевич', 'Кривоногих', 51, 1200)
    print(f'id = {e1.employee_id}, level = {e1.get_level()}, {e1.get_full_data()}')
