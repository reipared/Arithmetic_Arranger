def arithmetic_arranger(problems, show_answer=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ["", "", "", ""]
    for problem in problems:
        # Parse the problem string
        operands = problem.split()
        num1 = operands[0]
        operator = operands[1]
        num2 = operands[2]

        # Check if the operator is valid
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check if the operands are digits
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check if the operands have too many digits
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Compute the answer
        answer = str(eval(problem)) if show_answer else ""

        # Arrange the problem vertically
        width = max(len(num1), len(num2)) + 2
        arranged_problems[0] += num1.rjust(width)
        arranged_problems[1] += operator + num2.rjust(width - 1)
        arranged_problems[2] += "-" * width
        arranged_problems[3] += answer.rjust(width) if show_answer else ""

        # Add spacing between problems
        if problem != problems[-1]:
            for i in range(4):
                arranged_problems[i] += "    "

    # Combine the arranged problems into a single string
    arranged_str = "\n".join(arranged_problems)

    return arranged_str

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# Output:
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
# Output:
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474
