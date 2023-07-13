
from contextlib import suppress


def count(nt, x):  # defining the function with 2 inputs: a list and a variable
    count = 0  # to hold the number of count
    for i in nt:
        if i == x:  # we are iterating the list and checking if the element is equal to the given variable
            count += 1  # Add 1 to the count
    return count


def is_integer(x):
    if x % 1 == 0:  # an integer number is a number that is divisible by 1
        return True
    else:
        return False  # it is False


def pop(nt):
    a = nt[-1]  # Put the last element of the list into a variable
    del nt[-1]  # delete the last element of the list
    return a


# '''
# The tester doesn't work right in the is_cyclop function because it gives 44855090658 and expects True
#     but based on the program rules it should return a False
#     because only one or 3 zeros are acceptable
# '''


# def is_cyclops(n):
#     digits = str(n)  # turn the input nber into string
#     if len(digits) % 2 == 0:  # check if the len is even then it should return False; because a cyclops number should has an odd number of digits
#         return False
#     elif len(digits) % 2 != 0:
#         middle_nber = len(digits)//2  # to find the middle number
#         if digits[middle_nber] != '0':  # check the middle number if is equal to 0
#             return False
#         nt = list(digits)
#         zcount = count(nt, '0')  # to find the count of '0's in the list
#         if zcount == 1:  # check if the count of zero is 1
#             return True
#         elif zcount == 3:  # Check if the count of zeros is 3
#             # create a list of elements that contains the right hand of the number
#             part1 = [digits[x] for x in range(0, len(digits)//2)]
#             # create a list of elements which contains the left hand of the number
#             part2 = [digits[y] for y in range((len(digits)//2)+1, len(digits))]
#             # to check if all 3 three zeros are in their right places based on the question
#             if digits[middle_nber] == '0' and '0' in part1 and '0' in part2:
#                 return True
#             else:
#                 return False
#         else:
#             return False


def ztalloc(shape):
    x = 1  # initial x with first value of 1
    listed = list(shape)  # convert the string into the list
    while listed:  # while loop until the list becomes empty
        item = pop(listed)  # call pop function and give listed as a result
        if item == 'd':  # if the last element is down or 'd'
            prev = x*2  # when the item is down we have to find multiply 2
            # then we check if is the result integer or not
            check = is_integer(prev)  # check if the result is an integer or not
            if check == True:
                x = x*2
            else:
                return None
        elif item == 'u':  # check if the element is up or 'u'
            prev2 = (x-1)/3
            check = is_integer(prev2)
            if check == True:
                x = (x-1)/3
            else:
                return None
    if x == 0 or len(shape) == 0:
        return None
    t = ''
    n = x
    while len(t) < len(shape):  # the program should work until the len of string is less than the input
        if n % 2 == 0:
            n = n/2
            t = t+'d'
        elif n % 2 == 1:
            n = (3*n)+1
            t = t+'u'
    if t == shape:
        return int(x)
    else:
        return None


def count_troikas(items):
    TroikaCounter = 0
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            with suppress(Exception):  # check condition with error handeling function suppress
                k = j+(j-i)  # find the third same element
                c = j-i == k-j  # the condition to check troika
                if items[i] == items[j] == items[k] and c == True:
                    TroikaCounter += 1

    return TroikaCounter


def josephus(n,k):
    people=[] #a list to put people which includes indices
    eo=[] #the result 
    for i in range(1,n+1): # we loop through the n to create people
        people.append(i) 
    index=0 #initial index with zero 
    while n>0: # a condition to do statements below until n is equal to zero
        index=((index+k-1)%n) # a formula to calculate index
        eo.append(people.pop(index)) # When a person is killed he will be removed from the people list and add to the result list
        n-=1 # Every time we should decrease n

    return eo # finally return the result




#a function to find the reverse form of a list
def reverse(lst):
    # An empty list to hold the reverse form of the given list
    reversed_list = []
    for i in range(len(lst)):
        # removing the last element of the list and adding it to the reversed_list
        reversed_list.append(lst.pop())

    return reversed_list


def count_dominators(items):
    # If the number of the elements of the given list is zero then return 0 as the number of dominators
    if len(items) == 0:
        return 0
    # use the reverse function to return the reverse form of the list
    rev_items = reverse(items)
    # The first element of the reversed list is the max number to begin
    max = rev_items[0]
    # initial the count of the dominators with zero
    count = 0
    # iterate through the elements of the rev_items
    for x in rev_items:
        # if the element is bigger than max,put x value to max and add 1 to count
        if x > max:
            max = x
            count += 1
    # add 1 to the count(for a list with len>0 the smallest amount of the count is 1)and return
    return count+1


print(count_dominators([7, 51, 2, 22, 12, 4]))



RULES_110 = {  # Define a dictionary that maps tuples of binary values to new binary values according to the Rule 110 cellular automaton.
    (1, 1, 1): 0,
    (1, 1, 0): 1,
    (1, 0, 1): 1,
    (1, 0, 0): 0,
    (0, 1, 1): 1,
    (0, 1, 0): 1,
    (0, 0, 1): 1,
    (0, 0, 0): 0
}

def reverse_110(current):  # Define a function that takes a list of binary values as input.
    hold_dict = {}  # Create an empty dictionary to store previous results.
    number = len(current)  # Find the length of the input list.
    if tuple(current) in hold_dict:  # Check if the current list has been found before.
        return hold_dict[tuple(current)]  # If so, return the previously found result.

    def generate_exis():  # Define a generator function that yields all possible binary values of length 'number'.
        for i in range(2**number):
            yield tuple(int(digit) for digit in format(i, f'0{number}b'))

    exis_rules = []  # Create an empty list to store the new binary values for all possible combinations of binary values of length 'number'.
    for p in generate_exis():
        exis_rules.append(tuple(
            RULES_110[(p[(j-1) % number], p[j], p[(j+1) % number])] for j in range(number)))

    for key, value in zip(generate_exis(), exis_rules):  # Loop over all possible binary values of length 'number' and their corresponding new binary values.
        if len(key) == number and all(value[i] == current[i] for i in range(number)):  # If the new binary values match the input list, return the corresponding binary value.
            hold_dict[tuple(current)] = list(key)
            return list(key)

    return None  # If no matching binary value is found, return None.

print(reverse_110([1, 0, 1, 1]))  # Call the 'reverse_110' function with the input list [1, 0, 1, 1] and print the result.

def forbidden_digit(n, d):
    #initial variables
    count = 0
    number = 0
    while True:
        #check if the number has the digit d or not
        if str(d) not in str(number):
            #if the count equals n then we reached the answer
            if count == n:
                return number
            #otherwise increase the count
            count += 1
        #initial the variable i
        i = 1
        # another while loop to find the next number without the forbidden digit d. It starts with an increment of 1.
        while any(digit == str(d) for digit in str(number + i)):
            i += 1
        #increment number
        number += i
print(forbidden_digit(21,3))




def smetana_interpreter(program):
    #initialing the variables to hold the positions
    place_1 = 0
    place_2 = 0
    #the result variable
    steps = 0
    #to find the length of the given input
    length=len(program)
    while place_2 < length :
        #each statement in position place_2
        statement = program[place_2]
        #to check if the statement starts with GOTO
        if 'GOTO' in statement:
            #seperate the statement and find the next step
            next_statement = int(statement.split()[1])
            #update the positions
            place_2 = next_statement
            place_1 = next_statement
        #to check if the statement starts with SWAP
        elif 'SWAP' in statement:
            #seprating the statement to find the 2 steps which are going to replace
            x, y = map(int, statement.split()[1:])
            #switch  the steps
            program[x], program[y] = program[y], program[x]
            #incrementing the positions
            place_2 += 1
            place_1 += 1
        place_1 += 2
        #to check if there is an infinite loop or not
        if place_1 == place_2:
            return None
        #increment the steps every time
        steps += 1
        #to check if the number of steps is limited or not to avoid an infinite loop
        if steps > 1000:
            return None
    return steps
print(smetana_interpreter(['GOTO 2', 'SWAP 1 0', 'SWAP 2 1']))


def knight_survival(n, x, y, k):
    # Create a memoization table to store calculated probabilities
    arr = [[[-1] * (k+1) for _ in range(n)] for _ in range(n)]
    # If the first position of the knight is not in the bounds so return zero
    if not (0 <= x < n and 0 <= y < n):
        return '0'
    # a recursive function to calculate probabilities

    def probability_calculater(n, x, y, k):
        # If the number of moves becomes zero it should return 1
        if k == 0:
            return Fraction(1, 1)
        # An array to store probabilities of each move
        if arr[x][y][k] != -1:
            return arr[x][y][k]
        # initialize the p with 0
        probability = Fraction(0, 1)
        # a for loop to iterate over the possible moves
        for q, r in [(2, 1), (2, -1), (-2, 1), (-2, -1),
                     (1, 2), (1, -2), (-1, 2), (-1, -2)]:
            # create new variables and add the sum of each element of the possible moves to the first position of the knight.
            updated_x = x + q
            updated_y = y + r
            # check if the new positions are in the bound or not
            if 0 <= updated_x < n and 0 <= updated_y < n:
                # if so, find and update probability by calling the function recursively by giving new variables and incrementing the k
                probability += probability_calculater(n, updated_x,
                                                      updated_y, k-1) * Fraction(1, 8)
        # put the probability in each position
        arr[x][y][k] = probability
        return probability
    return probability_calculater(n, x, y, k)


def accumulate_dice(d, goal):
    # Initialize a list of probabilities with zero
    probabilities = [Fraction(0, 1)] * d
    # A list to hold the possible numbers of the die
    rolls = list(range(1, d + 1))
    # a recursive function to calculate probabilities

    def probability(total, rolls_left):
        # check if the total is equal to or greater than  the goal
        if total >= goal:
            # If so, add the probability of reaching the goal to the corresponding index in probabilities. and the probability is calculated.
            probabilities[total -
                          goal] += Fraction(1, d) ** (goal - rolls_left)
            return
        # a for loop to iterate rolls list
        for roll in rolls:
            # call the recursive function by updated inputs
            probability(total + roll, rolls_left - 1)
    probability(0, goal)
    return probabilities


"""An example for can_balance:
    consider we have list like items=[6,1,10,5,4]
    if i==0 ==> items[i]=6 ; so the left side will be 0 and the right side will be 1*1+10*2+5*3+4*4=52
            0!=52   ===> i=0 is not the answer so we increase the i
    if i==1 ==> left=6*1=6   right=10*1+5*2+4*3=32  ==> 6!=32 so increase the i 
    if i==2 ==> left=6*2+1*1=13   right=5*1+4*2=13   ==>13=13    so i is the answer

"""


def can_balance(items):
    # iterate through the range of the given list
    for i in range(len(items)):
        # a variable to compute left side of a specific element
        left = 0
        # a variable to compute right side of a specific element
        right = 0
        # iterate through the indices and values in each element of the list contains elements from 0 position to the ith position
        for m, n in enumerate(items[:i]):
            # calculate the distance each m from the ith element then multply it with the n for left side
            left += n * (i - m)
        # iterate through the indices and values in each element of the list contains elements from the next position after i to the last position
        for p, w in enumerate(items[i+1:]):
            # calculate the distance between each element in sublist from the i
            right += (p+(i+1)-i)*w
        # check if right and left were equal return the position
        if left == right:
            return i

    return None


""" An example for group_and_skip function:

    consider we have n=123456789, out= 10 , ins=1
    1)number of groups = 12345689//10=12345678 , reminder = 9 so we add 9 to the list:[9]
        update n with ins ===>n =number of groups * ins=12345678
    2)number of groups = 12345678//10=1234567 , reminder=8 add 8 to the result list ==> [9,8]
    .
    .
    .
    8)number of groups = 12//10=1 , reminder=2 add 2 to the list ==> [9,8,7,6,5,4,3,2]
    9)number of groups = 1//10=0 , reminder=1 add 1 to the list ==> [9,8,7,6,5,4,3,2,1]

"""


def group_and_skip(n, out, ins):
    # a list for holding the result numbers
    lst = []
    # each number which come out as reminder
    each = 0
    # iterate until the n is greater then 0
    while n > 0:
        # find the number of groups
        number_of_groups = n // out
        # find the reminder each time
        remainder = n % out
        # update the value
        each = remainder
        # add the value of "each" every time
        lst.append(each)
        # update n to have diffrent values through the while loop
        n = number_of_groups * ins
    # return the list
    return lst


""" An example for pyramid_blocks

    n=4 , m=2 , h=5
    result=0
    first layer=2*4=8    ==> result = 8
    second_layer=(2+1)(4+1)=15  ==> result=23
    third_layer=(2+2)(4+2)=24 ==> result=47
    forth_layer=(2+3)(4+3)=35 ==>result=82
    fifth_layer=(2+4)(4+4)=48  ==>result=130

"""
def pyramid_blocks(n, m, h):
    # a variable to hold the result
    result = 0
    # if we have only one layer the result woud be n times m
    if h == 1:
        result = n*m
    # otherwise we should iterate through the range of the h
    for i in range(h):
        # in erach layer the number of the row and columns are i units greater so we add i for row and column
        each_layer = ((n + i) * (m + i))
        # update the result
        result += each_layer
    return result


""" An Example for calkin_wilf function
    consider n=10
    lst=[(1,1)]
    1- pop (1,1) ==>lst=[]
        p=1 , lst=1
        lst.append((1,2))
        lst.append((2,1))
        lst=[(1,2),(2,1)]
        pivot=2
    2-pop (1,2) ==> lst=[(2,1)]
        p=1 , lst=2
        lst.append((1,3))
        lst.append((3,2))
        lst=[(2,1),(1,3),(3,2)]
        pivot=3
    3-pop(2,1) ==> lst=[(1,3),(3,2)]
        p=2 , lst=1
        lst.append((2,3))
        lst.append((3,1))
        lst=[(1,3),(3,2),(2,3),(3,1)]
        pivot=4
    4-pop((1,3)) ==> lst=[(3,2),(2,3),(3,1)]
        p=1 , lst=3
        lst.append((1,4))
        lst.append((4,3))
        lst=[(3,2),(2,3),(3,1),(1,4),(4,3)]
        pivot=5
    5-pop(3,2) ==> lst=[(2,3),(3,1),(1,4),(4,3)]
        p=3 , lst=2
        lst.append((3,5))
        lst.append((5,2))
        lst=[(2,3),(3,1),(1,4),(4,3),(3,5),(5,2)]
        pivot=6
    6-pop(2,3) ==> lst=[(3,1),(1,4),(4,3),(3,5),(5,2)]
        p=2 , lst=3
        lst.append(2,5)
        lst.append(5,3)
        lst=[(3,1),(1,4),(4,3),(3,5),(5,2),(2,5),(5,3)]
        pivot=7
    7-pop(3,1) ==> lst=[(1,4),(4,3),(3,5),(5,2),(2,5),(5,3)]
        p=3 , lst=1
        lst.append(3,4)
        lst.append(4,1)
        lst=[(1,4),(4,3),(3,5),(5,2),(2,5),(5,3),(3,4),(4,1)]
        pivot=8
    8-pop(1,4)  ==> lst=[(4,3),(3,5),(5,2),(2,5),(5,3),(3,4),(4,1)]
        p=1 , lst=4
        lst.append(1,5)
        lst.append(5,4)
        lst=[(4,3),(3,5),(5,2),(2,5),(5,3),(3,4),(4,1),(1,5),(5,4)]
        pivot=9
    9-pop(4,3)  ==> lst=[(3,5),(5,2),(2,5),(5,3),(3,4),(4,1),(1,5),(5,4)]
        p=4 , lst=3
        lst.append(4,7)
        lst.append(7,3)
        lst=[(3,5),(5,2),(2,5),(5,3),(3,4),(4,1),(1,5),(5,4),(4,7),(7,3)]
        pivot=10
    9<10 ==>  lst[0]=(3,5) ==>p,lst=lst[0] ==> p=3 and lst=5
    return 3/4

"""

#This defines a function called calkin_wilf that takes a single integer argument n.
def calkin_wilf(n):
    #initialize the first subsistence
    lst = [(1, 1)]
    #initialize pivot with 1
    pivot = 1
    while pivot < n:
        #pop the first tuple in the list and break it into 2 parts which represent nominator and dominator
        p, q = lst.pop(0)
        #To append two new tuples to the end of lst. The first tuple has p as the first element and p + lst as the second element. The second tuple has p + lst as the first element and lst as the second element
        lst.append((p, p + q))
        lst.append((p + q, q))
        #increase the pivot
        pivot += 1
    #break the first element of the list into nominators and dominators
    p, q = lst[0]
    #return the result
    return f'{p}/{q}'



print(calkin_wilf(10))
