from ArrayStack import ArrayStack

def eval_postfix_exp(exp_lst, vars):
    args_stack = ArrayStack()

    operators = "+-*/"

    for token in exp_lst:
        if (token not in operators):
            if token.isalpha():
                for var in vars:
                    if (token == var[0]):
                        args_stack.push(var[1])
            else:
                args_stack.push(int(token))

        else:
            arg2 = args_stack.pop()
            arg1 = args_stack.pop()
            if (token == "+"):
                res = arg1 + arg2
            if (token == "-"):
                res = arg1 - arg2
            if (token == "*"):
                res = arg1 * arg2
            if (token == "/"):
                if (arg2 == 0):
                    raise ZeroDivisionError
                else:
                    res = arg1/arg2
            args_stack.push(res)
    return args_stack.pop()

def interpreter_calculator():
    vars = []
    inp = input("--> ")
    while inp != "done()":

        exp_lst = str.split(inp)
        if len(exp_lst) > 2 and exp_lst[1] == "=":
                vars.append((exp_lst[0], eval_postfix_exp(exp_lst[2:], vars)))
                print(exp_lst[0])
        
        else: print(eval_postfix_exp(exp_lst, vars))
    
        inp = input("--> ")


def main():
    interpreter_calculator()

if __name__ == '__main__':
    main()