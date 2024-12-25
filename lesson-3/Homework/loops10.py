def sort_list(lst):
    sorted_lst = []
    while lst:
        min_val = lst[0]
        for item in lst:
            if item < min_val:
                min_val = item
        lst.remove(min_val)
        sorted_lst.append(min_val)
    return sorted_lst

# Example usage
my_list = [3, 1, 4, 5, 2]
print(f"The sorted list is {sort_list(my_list)}.")