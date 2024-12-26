def insert_element(lst, index, element):
    lst[index:index] = [element]
    return lst

# Example usage
my_list = [1, 2, 3, 5]
index_to_insert = 3
element_to_insert = 4
print(f"The list after insertion is {insert_element(my_list, index_to_insert, element_to_insert)}.")
