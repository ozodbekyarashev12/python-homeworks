def check_element(lst, element):
    for item in lst:
        if item == element:
            return True
    return False

# Example usage
my_list = [1, 2, 3, 4, 5]
element_to_check = 3
print(f"Is {element_to_check} in the list? {check_element(my_list, element_to_check)}.")
