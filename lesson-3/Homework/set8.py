def remove_element(my_set, element):
    my_set.discard(element)  # discard does not raise error if element doesn't exist
    return my_set

# Example usage
my_set = {1, 2, 3}
element = 2
print(remove_element(my_set, element))