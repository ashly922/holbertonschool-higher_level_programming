#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()

    # Iterate over each element in the input list
    for num in my_list:
        # Check if the element is an integer and add it to the set
        if isinstance(num, int):
            unique_integers.add(num)

    # Calculate the sum of unique integers in the set
    sum_unique = sum(unique_integers)

    return sum_unique
