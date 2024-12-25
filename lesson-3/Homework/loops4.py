def min_element(lst):
    min_val = lst[0]
    for item in lst:
        if item < min_val:
            min_val = item
    return min_val

# Example usage
my_list = [1, 2, 3, 4, 5]
print(f"The smallest element in the list is {min_element(my_list)}.")
