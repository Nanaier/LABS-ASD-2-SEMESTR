def input_sequence():
    stack_num = []
    print("Enter your sequence of even numbers\n to start new line press ENTER\n to end input enter '<'\n ")
    while True:
        line = input()
        if line[0] == "<":
            break
        else:
            for element in line.split():
                stack_num.append(int(element))

    return stack_num


def output(stack_num):
    print("resulting text:")
    for _ in stack_num[::-1]:
        top = stack_num.pop()
        if top > 0:
            print(top, end = " ")
    print()


stack = input_sequence()
output(stack)
