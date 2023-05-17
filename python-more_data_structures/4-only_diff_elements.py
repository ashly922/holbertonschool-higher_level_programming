#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create an empty set to store the unique elements
    unique = set()

    # Iterate over each element in the first set
    for elem in set_1:
        # Check if the element is not present in the second set
        if elem not in set_2:
            # Add the unique element to the set
            unique.add(elem)

    # Iterate over each element in the second set
    for elem in set_2:
        # Check if the element is not present in the first set
        if elem not in set_1:
            # Add the unique element to the set
            unique.add(elem)

    return unique
