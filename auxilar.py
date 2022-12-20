from py_expression_eval import Parser


class funt:
    def __init__(self, expression):
        self.exp = expression
        parser = Parser()
        v = parser.parse(expression)
        self.vars = v.variables()
        self.new_express = None

    def evaluate_params(self, params: dict):
        parser = Parser()
        x = parser.parse(self.exp)
        self.new_express = x.simplify(params).toString()

    def evaluate(self, x, y, t=0):
        parser = Parser()
        return parser.evaluate(self.new_express, {'x': x, 'y': y, 't': t})

    def string(self):
        return self.new_express


class fun:
    def __init__(self, function, params):
        self.function = function
        self.params = params

    def call(self, x, y, t=0):
        return self.function(x, y, t, self.params)

    def Change_params(self, params):
        self.params = params

class SystemEdos:
    def __init__(self,f,g):
        self.f = f
        self.g = g
      
    def evaluate(self,Y ,t=0):
        x, y = Y
        return [self.f(x,y,t),self.g(x,y,t)]
    