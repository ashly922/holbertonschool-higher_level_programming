#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    result = []

    # Iterate over each element in the input list
    for element in my_list:
        # Check if the element matches the search element
        if element == search:
            # If it matches, add the replace element to the result list
            result.append(replace)
        else:
            # If it doesn't match, add the original element to the result list
            result.append(element)

    return result
