#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Create an empty set to store the common elements
    common = set()

    # Iterate over each element in the first set
    for elem in set_1:
        # Check if the element is present in the second set
        if elem in set_2:
            # Add the common element to the set
            common.add(elem)

    return common
