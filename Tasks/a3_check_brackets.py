def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    my_brackets_stack = []
    count = 0
    for i in brackets_row:
        if i == "(":
            count += 1
            my_brackets_stack.append(i)
        if i == ")":
            count -= 1
            if count < 0:
                return False
    return count == 0
