class Add:
    def execute(self, a, b):
        return a + b

class Subtract:
    def execute(self, a, b):
        return a - b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, a, b):
        return self.strategy.execute(a, b)

context_add = Context(Add())
print(context_add.execute_strategy(10, 5))

context_sub = Context(Subtract())
print(context_sub.execute_strategy(10, 5))
