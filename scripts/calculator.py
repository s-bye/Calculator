class Calculator:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, value):
        self.expression += str(value)

    def clear_expression(self):
        self.expression = ""

    def evaluate_expression(self):
        try:
            if "%" in self.expression:
                self.expression = self.expression.replace("%", "/100")
            result = eval(self.expression)
            self.expression = str(result)
            return result
        except Exception as e:
            self.expression = ""
            return "Error"