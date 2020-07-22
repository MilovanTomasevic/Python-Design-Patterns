## Interpreter Coding Exercise
You are asked to write an expression processor for simple numeric expressions with the following constraints:

- Expressions use integral values (e.g., `'13'` ), single-letter variables defined in Variables, as well as + and - operators only
- There is no need to support braces or any other operations
- If a variable is not found in `variables`  (or if we encounter a variable with >1 letter, e.g. ab), the evaluator returns 0 (zero)
- In case of any parsing failure, evaluator returns 0

Example:
- `calculate("1+2+3")`  should return 6
- `calculate("1+2+xy")`  should return 0
- `calculate("10-2-x")`  when x=3 is in `variables`  should return 5