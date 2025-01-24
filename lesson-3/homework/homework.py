# List Tasks
def count_occurrences(lst, element):
    return lst.count(element)

def sum_of_elements(lst):
    return sum(lst)

def max_element(lst):
    return max(lst)

def min_element(lst):
    return min(lst)

def check_element(lst, element):
    return element in lst

def first_element(lst):
    return lst[0] if lst else None

def last_element(lst):
    return lst[-1] if lst else None

def slice_list(lst):
    return lst[:3]

def reverse_list(lst):
    return lst[::-1]

def sort_list(lst):
    return sorted(lst)

def remove_duplicates(lst):
    return list(set(lst))

def insert_element(lst, element, index):
    lst.insert(index, element)
    return lst

def index_of_element(lst, element):
    return lst.index(element) if element in lst else None

def check_empty_list(lst):
    return len(lst) == 0

def count_even_numbers(lst):
    return sum(1 for x in lst if x % 2 == 0)

def count_odd_numbers(lst):
    return sum(1 for x in lst if x % 2 != 0)

def concatenate_lists(lst1, lst2):
    return lst1 + lst2

def find_sublist(lst, sublist):
    return str(sublist) in str(lst)

def replace_element(lst, old, new):
    if old in lst:
        lst[lst.index(old)] = new
    return lst

def find_second_largest(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[-2] if len(lst) > 1 else None

def find_second_smallest(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[1] if len(lst) > 1 else None

def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def list_length(lst):
    return len(lst)

def create_copy(lst):
    return lst.copy()

def get_middle_element(lst):
    length = len(lst)
    if length % 2 == 0:
        return lst[length // 2 - 1: length // 2 + 1]
    return lst[length // 2]

def find_max_of_sublist(lst, start, end):
    return max(lst[start:end])

def find_min_of_sublist(lst, start, end):
    return min(lst[start:end])

def remove_element_by_index(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
    return lst

def check_if_sorted(lst):
    return lst == sorted(lst)

def repeat_elements(lst, n):
    return [x for x in lst for _ in range(n)]

def merge_and_sort(lst1, lst2):
    return sorted(lst1 + lst2)

def find_all_indices(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

def rotate_list(lst, n):
    return lst[-n:] + lst[:-n]

def create_range_list(start, end):
    return list(range(start, end + 1))

def sum_of_positive_numbers(lst):
    return sum(x for x in lst if x > 0)

def sum_of_negative_numbers(lst):
    return sum(x for x in lst if x < 0)

def check_palindrome(lst):
    return lst == lst[::-1]

def create_nested_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

def get_unique_elements_in_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# Tuple Tasks
def count_occurrences_in_tuple(tpl, element):
    return tpl.count(element)

def max_element_in_tuple(tpl):
    return max(tpl)

def min_element_in_tuple(tpl):
    return min(tpl)

def check_element_in_tuple(tpl, element):
    return element in tpl

def first_element_in_tuple(tpl):
    return tpl[0] if tpl else None

def last_element_in_tuple(tpl):
    return tpl[-1] if tpl else None

def tuple_length(tpl):
    return len(tpl)

def slice_tuple(tpl):
    return tpl[:3]

def concatenate_tuples(tpl1, tpl2):
    return tpl1 + tpl2

def check_if_tuple_is_empty(tpl):
    return len(tpl) == 0

def get_all_indices_of_element_in_tuple(tpl, element):
    return [i for i, x in enumerate(tpl) if x == element]

def find_second_largest_in_tuple(tpl):
    sorted_tpl = sorted(tpl)
    return sorted_tpl[-2] if len(tpl) > 1 else None

def find_second_smallest_in_tuple(tpl):
    sorted_tpl = sorted(tpl)
    return sorted_tpl[1] if len(tpl) > 1 else None

def create_single_element_tuple(element):
    return (element,)

def convert_list_to_tuple(lst):
    return tuple(lst)

def check_if_tuple_is_sorted(tpl):
    return tpl == tuple(sorted(tpl))

def find_max_of_subtuple(tpl, start, end):
    return max(tpl[start:end])

def find_min_of_subtuple(tpl, start, end):
    return min(tpl[start:end])

def remove_element_by_value_in_tuple(tpl, element):
    tpl = list(tpl)
    if element in tpl:
        tpl.remove(element)
    return tuple(tpl)

def create_nested_tuple(tpl, size):
    return tuple(tpl[i:i + size] for i in range(0, len(tpl), size))

def repeat_elements_in_tuple(tpl, n):
    return tpl * n

def create_range_tuple(start, end):
    return tuple(range(start, end + 1))

def reverse_tuple(tpl):
    return tpl[::-1]

def check_palindrome_in_tuple(tpl):
    return tpl == tpl[::-1]

def get_unique_elements_in_tuple(tpl):
    seen = set()
    return tuple(x for x in tpl if not (x in seen or seen.add(x)))

# Set Tasks
def union_of_sets(set1, set2):
    return set1 | set2

def intersection_of_sets(set1, set2):
    return set1 & set2

def difference_of_sets(set1, set2):
    return set1 - set2

def check_subset(set1, set2):
    return set1 <= set2

def check_element_in_set(set1, element):
    return element in set1

def set_length(set1):
    return len(set1)

def convert_list_to_set(lst):
    return set(lst)

def remove_element_from_set(set1, element):
    set1.discard(element)
    return set1

def clear_set(set1):
    set1.clear()
    return set1

def check_if_set_is_empty(set1):
    return len(set1) == 0

def symmetric_difference(set1, set2):
    return set1 ^ set2

def add_element_to_set(set1, element):
    set1.add(element)
    return set1

def pop_element_from_set(set1):
    return set1.pop() if set1 else None

def find_max_in_set(set1):
    return max(set1)

def find_min_in_set(set1):
    return min(set1)

def filter_even_numbers_in_set(set1):
    return {x for x in set1 if x % 2 == 0}

def filter_odd_numbers_in_set(set1):
    return {x for x in set1 if x % 2 != 0}

def create_set_of_range(start, end):
    return set(range(start, end + 1))

def merge_and_deduplicate_lists(lst1, lst2):
    return set(lst1 + lst2)

def check_disjoint_sets(set1, set2):
    return set1.isdisjoint(set2)

def remove_duplicates_from_list(lst):
    return list(set(lst))

def count_unique_elements(lst):
    return len(set(lst))


import random
def generate_random_set(n, start, end):
    return {random.randint(start, end) for _ in range(n)}

# Dictionary Tasks
def get_value(dct, key):
    return dct.get(key, None)

def check_key(dct, key):
    return key in dct

def count_keys(dct):
    return len(dct)

def get_all_keys(dct):
    return list(dct.keys())

def get_all_values(dct):
    return list(dct.values())

def merge_dictionaries(dct1, dct2):
    return {**dct1, **dct2}

def remove_key(dct, key):
    if key in dct:
        del dct[key]
    return dct

def clear_dictionary(dct):
    dct.clear()
    return dct

def check_if_dictionary_is_empty(dct):
    return len(dct) == 0

def get_key_value_pair(dct, key):
    return (key, dct[key]) if key in dct else None

def update_value(dct, key, value):
    dct[key] = value
    return dct

def count_value_occurrences(dct, value):
    return list(dct.values()).count(value)

def invert_dictionary(dct):
    return {v: k for k, v in dct.items()}

def find_keys_with_value(dct, value):
    return [k for k, v in dct.items() if v == value]

def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

def check_for_nested_dict(dct):
    return any(isinstance(v, dict) for v in dct.values())

def get_nested_value(dct, outer_key, inner_key):
    return dct.get(outer_key, {}).get(inner_key, None)

def create_default_dict(default_value):
    from collections import defaultdict
    return defaultdict(lambda: default_value)

def count_unique_values(dct):
    return len(set(dct.values()))

def sort_dict_by_key(dct):
    return dict(sorted(dct.items()))

def sort_dict_by_value(dct):
    return dict(sorted(dct.items(), key=lambda item: item[1]))

def filter_dict_by_value(dct, condition):
    return {k: v for k, v in dct.items() if condition(v)}

def check_for_common_keys(dct1, dct2):
    return bool(set(dct1.keys()) & set(dct2.keys()))

def create_dict_from_tuple(tpl):
    return dict(tpl)

def get_first_key_value_pair(dct):
    return next(iter(dct.items()), None)
