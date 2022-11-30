import random


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


def e_counter(word):
    sum_e = 0
    for character in word:
        if character == 'e':
            sum_e += 1
    return sum_e


def operation1(n):
    '''Add the first n numbers.'''
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return sum


def operation2(n):
    '''Multiply the first n numbers.'''
    product = 1
    for i in range(1, n + 1):
        product = product * i
        # print(product)
    return product


def operation3():
    '''Cummulatively concatenate onto a string.'''
    my_grades = [4, 3, 2, 3, 3, 4]
    my_string = "The grades are: "
    for i in range(len(my_grades) - 1):
        my_string = my_string + str(my_grades[i]) + ', '
    my_string += f'{str(my_grades[-1])}.'
    return my_string


def timesTable():
    for i in range(1, 13):
        print(f'1 * {i} = {1 * i}')


def timesTable2():
    for i in range(1, 13):
        for j in range(1, 13):
            print(f'{i} * {j} = {i * j}')


# Recursion is another way to write indefinite loops besides while.

def maze():
    '''Remain lost if you turn left and
    fall in a pit if you do anything else.'''
    response = 'left'
    while response == 'left':
        response = input("You are lost in a scary maze. "
                         "Will you go left or right? ")
    print("You fall in a pit. You lose.")


# Recursive actions invoke themselves.
# You will write functions that call themselves.
def maze2():
    '''Use recursion to remain lost if you turn left and
        fall in a pit if you do anything else.'''
    # INITIALIZE the variable response
    # and subsequently update it.
    response = input("You are lost in a scary maze. "
                     "Will you go left or right? ")
    # Define a STOP condition.
    if response != 'left':
        print("You fall in a pit. You lose.")
    else:
        # Have the function CALL ITSELF.
        maze2()


# Functions written with while can be rewritten recursion and vice versa.
def guess_number():
    '''Prompt the user to guess a number between 1 and 10.
    Prompt for higher or lower as needed.
    Report when the guess is correct.'''
    # Generate the random number to be guessed.
    answer = random.randrange(10) + 1
    guess = int(input("Guess a number between 1 and 10. "))
    while guess != answer:
        if guess < answer:
            guess = int(input("Guess higher! "))
        else:
            guess = int(input("Guess lower! "))
    print("You guessed it!")


def guess_number2():
    '''Prompt the user to guess a number between 1 and 10.
    Prompt for higher or lower as needed.
    Report when the guess is correct. Use recursion.'''
    # Generate the random number to be guessed.
    answer = random.randrange(10) + 1
    guess = int(input("Guess a number between 1 and 10. "))
    try_it(answer, guess)


def try_it(answer, guess):
    if guess == answer:
        print("You guessed it!")
    elif guess < answer:
        guess = int(input("Guess higher! "))
        try_it(answer, guess)
    else:
        guess = int(input("Guess lower! "))
        try_it(answer, guess)


def countdown_recursive(number):
    # Define a STOP condition.
    if number < 0:
        print("Blastoff!")
    else:
        print(number)
        countdown_recursive(number - 1)


# This function contains a common error!
# Put the stop condition in an if
# and then put the recursive call in an else block.

def countdown_recursive2(number):
    print(number)
    countdown_recursive2(number - 1)
    # Define a STOP condition.
    if number < 0:
        print("Blastoff!")


# An alternative to a stop condition is a go condition.
def countdown_recursive3(number):
    # Define a GO condition.
    if number >= 0:
        print(number)
        countdown_recursive(number - 1)
    else:
        print("Blastoff!")


# What is the error in this version?
def countdown_recursive_wrong(number):
    # Define a GO condition.
    if number >= 0:
        print(number)
        countdown_recursive_wrong(number - 1)
    print("Blastoff!")


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
    # loop6("excellent")
    # print(f'There are {e_counter("excellent")} letters "e" in "excellent".')
    # print(f'There are {e_counter("juice")} letters "e" in "juice".')
    # print(f'There are {e_counter("froggy")} letters "e" in "froggy".')
    # print(operation1(6))
    # print(operation2(6))
    # print(operation3())
    # timesTable()
    # timesTable2()
    # maze()
    # maze2()
    # guess_number()
    # guess_number2()
    countdown_recursive_wrong(3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
