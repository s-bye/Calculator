class Calculator:
    def __init__(self):
        self.current_value = 0
        self.operator = None
        self.operand = ""

    def clear(self):
        self.current_value = 0
        self.operator = None
        self.operand = ""

    def set_operand(self, value):
        self.operand += str(value)

    def set_operator(self, operator):
        if self.operand:
            self.calculate()
        self.operator = operator

    def calculate(self):
        if self.operand:
            operand_value = int(self.operand)
            if self.operator == "+":
                self.current_value += operand_value
            elif self.operator == "-":
                self.current_value -= operand_value
            elif self.operator == "*":
                self.current_value *= operand_value
            elif self.operator == "/":
                if operand_value != 0:
                    self.current_value /= operand_value
                else:
                    self.current_value = "Error"
            elif self.operator == "%":
                self.current_value %= operand_value
            else:
                self.current_value = operand_value
            self.operator = None
            self.operand = ""

    def get_current_value(self):
        return self.current_value
