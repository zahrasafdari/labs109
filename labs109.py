
# from contextlib import suppress


# def count(nt, x):  # defining the function with 2 inputs: a list and a variable
#     count = 0  # to hold the nber of count
#     for i in nt:
#         if i == x:  # we are iterating the list and check if the element is equal to the given variable
#             count += 1  # add 1 to the count
#     return count


# def is_integer(x):
#     if x % 1 == 0:  # an integer nber is a nber that is divisible by 1
#         return True
#     else:
#         return False  # it is False


# def pop(nt):
#     a = nt[-1]  # put the last element of the list into a variable
#     del nt[-1]  # delete the last element of the list
#     return a


# # '''
# #     the tester doesnt work right in is_cyclop function because it gives 44855090658 and expect True
# #     but base on the program rules it should return False
# #     because only one or 3 zeros are acceptable
# # '''


# # def is_cyclops(n):
# #     digits = str(n)  # turn the input nber into string
# #     if len(digits) % 2 == 0:  # check if the len is even then it should return False;because a cyclope nber should has an odd nber of digits
# #         return False
# #     elif len(digits) % 2 != 0:
# #         middle_nber = len(digits)//2  # to find the middle nber
# #         if digits[middle_nber] != '0':  # check the middle nber if is equal to 0
# #             return False
# #         nt = list(digits)
# #         zcount = count(nt, '0')  # to find the count of '0's in the list
# #         if zcount == 1:  # check if the count of zero is 1
# #             return True
# #         elif zcount == 3:  # check if the count of zeros is 3
# #             # create a list of elements which contains the right hand of the nber
# #             part1 = [digits[x] for x in range(0, len(digits)//2)]
# #             # create a list of elements which contains the left hand of the nber
# #             part2 = [digits[y] for y in range((len(digits)//2)+1, len(digits))]
# #             # to check if all 3 three zeros are in their right places based on the question
# #             if digits[middle_nber] == '0' and '0' in part1 and '0' in part2:
# #                 return True
# #             else:
# #                 return False
# #         else:
# #             return False


# def ztalloc(shape):
#     x = 1  # initial x with first value of 1
#     listed = list(shape)  # convert the string into the list
#     while listed:  # while loop until the list become empty
#         item = pop(listed)  # call pop funtion and give listed as a result
#         if item == 'd':  # if the last element is down or 'd'
#             prev = x*2  # when item is down we have to find multipy 2
#             # then we check if is the result integer or not
#             check = is_integer(prev)  # check if the result is integer or not
#             if check == True:
#                 x = x*2
#             else:
#                 return None
#         elif item == 'u':  # check if the element is up or 'u'
#             prev2 = (x-1)/3
#             check = is_integer(prev2)
#             if check == True:
#                 x = (x-1)/3
#             else:
#                 return None
#     if x == 0 or len(shape) == 0:
#         return None
#     t = ''
#     n = x
#     while len(t) < len(shape):  # the program should work until the len of string is less than the input
#         if n % 2 == 0:
#             n = n/2
#             t = t+'d'
#         elif n % 2 == 1:
#             n = (3*n)+1
#             t = t+'u'
#     if t == shape:
#         return int(x)
#     else:
#         return None


# def count_troikas(items):
#     TroikaCounter = 0
#     for i in range(len(items)):
#         for j in range(i+1, len(items)):
#             with suppress(Exception):  # check condition with error handeling function suppress
#                 k = j+(j-i)  # find the third same element
#                 c = j-i == k-j  # the condition to check troika
#                 if items[i] == items[j] == items[k] and c == True:
#                     TroikaCounter += 1

#     return TroikaCounter


def josephus(n,k):
    people=[] #a list to put people which includes indices
    eo=[] #the result 
    for i in range(1,n+1): # we loop through the n to create people
        people.append(i) 
    index=0 #initial index with zero 
    while n>0: # a condition to do statments below until n is equal to zero
        index=((index+k-1)%n) # a formula to calculate index
        eo.append(people.pop(index)) # when a person killed he will be remove from the people list and add to result list
        n-=1 # every time we should decrease n

    return eo # finally return the result




#a function to find the reverse form of a list
def reverse(lst):
    # an empty list to hold the reverse form of the given list
    reversed_list = []
    for i in range(len(lst)):
        # removing the last element of the list and adding if to the reversed_list
        reversed_list.append(lst.pop())

    return reversed_list


def count_dominators(items):
    # if the number of the elements of the given list is zero then return 0 as the number of dominators
    if len(items) == 0:
        return 0
    # use the reverse function to return the reverse form of the list
    rev_items = reverse(items)
    # the first element of the reversed list is the max number to begin
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
    hold_dict = {}  # Create an empty dictionary to store previously results.
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

