# ExpressionTree

## Function

* parse expression string which only contain number(can be natural number, decimal number), "+", "-", "*", "/", "(", ")" to a expression tree
* evaluate a express tree

## How to use

frist you should import the file

then you can create a expression class instance

`e = Expression("4*4-4.4/1")`

next you can convert the expression to a expression tree

`t = e.convert_expression()`

now you can evaluate the express tree value

`print t.evaluate()`