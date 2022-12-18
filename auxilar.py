from py_expression_eval import Parser

class funt:
   def __init__(self,expression):
    self.exp=expression
    parser=Parser()
    v=parser.parse(expression)
    self.vars=v.variables()
    self.new_express=None
    
   def evaluate_params(self,params:dict):
     parser=Parser()
     x=parser.parse(self.exp)
     self.new_express=x.simplify(params).toString()
    
   def evaluate(self,x,y,t):
     parser=Parser()
     return parser.evaluate(self.new_express,{'x':x,'y':y,'t':t})
    
   def string(self):
     return self.new_express