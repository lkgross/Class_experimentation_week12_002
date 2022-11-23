# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def loop1():
    '''Use a standard loop with range(10).'''
    for i in range(10):
        print(i)


def loop2(starting_loop_variable_value):
    '''Use a parameter for the starting value of a loop.'''
    for i in range(starting_loop_variable_value, 10):
        print(i)


def loop3():
    '''Call range with three arguments 1, 10, and 2.'''
    for i in range(1, 10, 2):
        print(i)


def loop4(starting_value, ending_upper_bound, step_size):
    '''Call range with parameters for the starting value, the upper
    bound on the sequence, and the step size.'''
    for i in range(starting_value, ending_upper_bound, step_size):
        print(i)


def loop5():
    '''Print a message each time you encounter an 'e' in 'excellent'.'''
    for i in range(9):
        if "excellent"[i] == "e":
            print("There is an 'e' in 'excellent'.")


def loop6(word):
    '''Print whether or not or not there is an 'e' in word.'''
    any_e = False
    i = 0
    while (i < len(word)) and (any_e == False):
        if word[i] == "e":
            print(f"There is an 'e' in {word}.")
            any_e = True
        else:
            # i = i + 1
            # An alternate syntax is
            i += 1
    if (i == len(word)):
        print(f"There is no 'e' in {word}.")


def operation1(n):
    '''Add the first n numbers.'''
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return sum


def timesTable():
    for i in range(1, 13):
        print(f'1 * {i} = {1 * i}')

def timesTable2():
    for i in range(1, 13):
        for j in range(1, 13):
            print(f'{i} * {j} = {i * j}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # print_hi('Laura')
    # loop1()
    # loop2(2)
    # loop3()
    # loop4(2, 13, 2)
    # loop5()
    # loop6("froggy")
    # loop6("juice")
    # print(operation1(5))
    # timesTable()
    timesTable2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
