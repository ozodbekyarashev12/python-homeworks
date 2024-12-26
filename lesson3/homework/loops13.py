def index_of_element(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1

# Example usage
my_list = [1, 2, 3, 4, 5]
element_to_find = 3
print(f"The index of {element_to_find} in the list is {index_of_element(my_list, element_to_find)}.")