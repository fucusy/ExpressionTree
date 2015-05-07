#!encoding=utf8
__author__ = 'user'
from helper import *


class Expression():
    s = ""
    index = 0
    operators = ["+","-","*","/",")","("]

    def __init__(self):
        self.index = 0

    def __init__(self, s):
        self.s = s
        self.index = 0

    def get_next(self):
        s = self.s
        if self.index < len(s):
            if s[self.index] in self.operators:
                r = s[self.index]
                self.index += 1
                return r
            else:
                next_index = self.index + 1
                while next_index <= len(s) and is_numeric(s[self.index:next_index]):
                    next_index += 1
                r = s[self.index:next_index-1]
                self.index = next_index - 1
                return r
        return ""

    def convert_expression(self):
        operation_stack = []
        number_stack = []
        next_v = self.get_next()
        while next_v != "":
            if next_v in self.operators:
                if len(operation_stack) > 0:
                    pre_op = operation_stack.pop()
                    if next_v == "+" or next_v == "-" or ((next_v == "*" or next_v == "/" ) and ( pre_op == "*" or pre_op == "/")):
                        num_right = number_stack.pop()
                        num_left = number_stack.pop()
                        if num_right.__class__.__name__ == Expression.__name__:
                            num_right_tree = num_right
                        else:
                            num_right_tree = ExpressionTree(num_right)
                        if num_left.__class__.__name__ == Expression.__name__:
                            num_left_tree = num_left
                        else:
                            num_left_tree = ExpressionTree(num_left)
                        last = ExpressionTree(pre_op)
                        last.left_tree = num_left_tree
                        last.right_tree = num_right_tree
                        number_stack.append(last)
                        operation_stack.append(next_v)
                    elif (next_v == "*" or next_v == "/" ) and ( pre_op == "+" or pre_op == "-"):
                        operation_stack.append(pre_op)
                        operation_stack.append(next_v)
                else:
                    operation_stack.append(next_v)

            elif is_numeric(next_v):
                number_stack.append(next_v)

            next_v = self.get_next()

        # 经过上述操作之后，乘号或者除号，只可能在符号栈也就是operation_stack的顶部，
        # 下面检查符号栈顶部符号，除去可能的最后一个乘号或者除号
        if operation_stack[len(operation_stack) - 1] == "/" or operation_stack[len(operation_stack) - 1] == "*":
            last_op = operation_stack.pop()
            num_right = number_stack.pop()
            num_left = number_stack.pop()
            if num_right.__class__.__name__ == Expression.__name__:
                num_right_tree = num_right
            else:
                num_right_tree = ExpressionTree(num_right)
            if num_left.__class__.__name__ == Expression.__name__:
                num_left_tree = num_left
            else:
                num_left_tree = ExpressionTree(num_left)

            last = ExpressionTree(last_op)
            last.left_tree = num_left_tree
            last.right_tree = num_right_tree
            number_stack.append(last)

        # 经过上面的检查，最后，符号栈中不可能存在，"*" 和 "/" 了
        # 因为，符号栈中只可能存在，"+" 与 "-",
        # 他们的优先级一致时计算，我们要保持从左到右进行计算，因此，对符号栈，和数字栈进行正反颠倒
        operation_stack.reverse()
        number_stack.reverse()

        # check the number stack
        while( len(operation_stack) != 0 ):

            left = number_stack.pop()
            right = number_stack.pop()


            if right.__class__.__name__ == ExpressionTree.__name__:
                right_tree = right
            else:
                right_tree = ExpressionTree(right)

            if left.__class__.__name__ == ExpressionTree.__name__:
                left_tree = left
            else:
                left_tree = ExpressionTree(left)

            last = ExpressionTree(operation_stack.pop())
            last.right_tree = right_tree
            last.left_tree = left_tree
            number_stack.append(last)

        if len(number_stack) > 0:
            return number_stack.pop()
        else:
            return None

class ExpressionTree():
    left_tree = None
    right_tree = None
    val = None
    op = None

    def __init__(self, s):
        if s in Expression.operators:
            self.op = s
        elif is_numeric(s):
            self.val = convert_string_to_numeric(s)

    def evaluate(self):
        if self.right_tree is None and self.left_tree is None:
            return self.val
        else:
            if self.op == "+":
                return self.left_tree.evaluate() + self.right_tree.evaluate()
            if self.op == "-":
                return self.left_tree.evaluate() - self.right_tree.evaluate()
            if self.op == "*":
                return self.left_tree.evaluate() * self.right_tree.evaluate()
            if self.op == "/":
                return self.left_tree.evaluate() / self.right_tree.evaluate()
if __name__ == '__main__':
    e = Expression("1-2*3")
    t = e.convert_expression()
    print t.evaluate()
