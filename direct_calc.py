# encoding=utf8
"""
modified from https://github.com/eryueniaobp/leetcode/blob/master/string%20algorithm/Calculator.cpp
2012-5-21 Google面试第三轮

给出表达式，求最后的值  +- /* ()
思路：
    ) 不入栈
        遇到 ),就计算当前 ( ) 内的值，并弹出 (
    num_stack - 存储数字
    op_stack -- 存储(及+ - * /
    op需要向右看一位 ,如果右面的优先级较高的话，就先入栈；
        否则，就计算前面的数字
"""


def ready2cal(cur, nex):
    add_sub = ['+', '-']
    mul_div = ['/', '*']
    if cur in add_sub:
        return next in add_sub
    elif cur in mul_div:
        return True
    elif cur == '(':
        return False


def cal_top2(num_stack, op_stack):
    op = op_stack.pop()
    num2 = num_stack.pop()
    num1 = num_stack.pop()
    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '/':
        res = num1 / num2
    else:
        res = num1 * num2
    num_stack.append(res)


def calc(exp):
    op_list = ['+', '-', '*', '/']
    num_stack = []
    op_stack = []
    i = 0
    while i < len(exp):
        if exp[i].isdigit():
            tmp = 0
            while i < len(exp) and exp[i].isdigit():
                tmp = 10 * tmp + int(exp[i])
                i += 1
            num_stack.append(tmp)
            continue
        elif exp[i] in op_list:
            if len(op_stack) == 0 or not ready2cal(op_stack[-1], exp[i]):
                op_stack.append(exp[i])
            else:
                cal_top2(num_stack, op_stack)
                op_stack.append(exp[i])
        elif exp[i] == '(':
            op_stack.append(exp[i])
        elif exp[i] == ')':
            while op_stack[-1] != '(':
                cal_top2(num_stack, op_stack)
            # pop (
            op_stack.pop()
        i += 1
    while len(op_stack) > 0:
        cal_top2(num_stack, op_stack)
    return num_stack[0]


if __name__ == '__main__':
    test_case = ["7+8*5*(9-8) ", "7*8+9", "(((7*8+9))) ", "7*(9-8)"\
            , "6*((5-4)+(7-6))", "7+8*(9-5)", "(7+8*2)*2"]
    test_ans = [47, 65, 65, 7, 12, 39, 46]
    for i, case in enumerate(test_case):
        if calc(case) == test_ans[i]:
            print("right:%s = %s" % (case, test_ans[i]))
        else:
            print("right:%s = %s, not %s" % (case, test_ans[i], calc(case)))
