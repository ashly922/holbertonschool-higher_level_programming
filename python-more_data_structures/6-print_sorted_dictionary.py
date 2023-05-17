#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get the sorted keys of the dictionary
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate over the sorted keys
    for key in sorted_keys:
        # Print the key-value pair
        print("{}: {}".format(key, a_dictionary[key]))
