from utils.tools import operator_str


class Neuron:

    def __init__(self, action, condition):
        self.action = action
        self.condition = condition

    def __str__(self):
        return f"{self.condition} - {self.action}"

    @staticmethod
    def display_signal(condition, row):
        print(
            f"{condition.attr} "
            f"{row[condition.attr]} "
            f"{operator_str(condition.operator)} "
            f"{condition.value}"
        )

    def signal(self, row):
        if self.condition.evaluate(row):
            self.display_signal(self.condition, row)
            self.action.event(row)
