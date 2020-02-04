class Worker:

    def __init__(self, name, surname, position, income_wage, income_bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': income_wage, 'bonus': income_bonus}

class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


worker_1 = Position("Ivan", "Ivanov", 'dir', 500, 100)
worker_1.get_full_name()
worker_1.get_total_income()
