# Visitor Coding Exercise
You are asked to implement a visitor called `ExpressionPrinter`  for printing different mathematical expressions. The range of expressions covers addition and multiplication - please put round brackets around addition operations (but not multiplication ones)! Also, please avoid any blank spaces in output.

Example:
- Input: `AdditionExpression(Value(2), Value(3))` 
- Output: `(2+3)` 

Here is the corresponding unit test:

```py
class Evaluate(unittest.TestCase):
    def test_simple_addition(self):
        simple = AdditionExpression(Value(2), Value(3))
        ep = ExpressionPrinter()
        ep.visit(simple)
        self.assertEqual("(2+3)", str(ep))
```