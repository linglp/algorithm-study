# finding the smallest element in two lists
lst_one = [2, 5, 1]
lst_two = [10, 9, 8]

smallest = lst_one[0]


i = 0
while i < len(lst_one):
    if lst_one[i] < lst_two[i]:
        smallest = lst_one[i]
    else:
        smallest = smallest
    i = i +1



# assume two lists are sorted, how could I order a new list based on the elements within each list

# some items in list b are bigger than list a
lst_a = [9, 11, 20, 99]
lst_b = [6, 8, 21, 1000]

# all items in list b are bigger than list a
lst_c = [4, 5, 6, 7]
lst_d = [9, 100, 200, 300]

# all items in list b are bigger than list a
lst_e = [9, 100, 200, 300]
lst_f = [4, 5, 6, 7]

# another mix list
lst_g = [9, 11, 20, 9900]
lst_h = [6, 80, 210, 1000]


def filter_list(lst_one, lst_two):
    return [x for x in lst_one if x not in lst_two]

def save_result_to_dict(dict_storage, lst_one_elem, lst_two_elem):

    try:
        dict_storage[lst_one_elem].append(lst_two_elem)
    except: 
        dict_storage[lst_one_elem] = [lst_two_elem]
      
def get_index_and_lst_to_insert(new_lst, lst_one_elem_key, value):
    # since all elements in lst one are already in the new list
    # find the index to insert based on position of list one element
    index_to_insert = new_lst.index(lst_one_elem_key)

    # only insert items that are not already in new_lst
    new_items = filter_list(value, new_lst)
    return index_to_insert, new_items


def merge_sort(lst_one, lst_two):
    new_lst = lst_one.copy()

    # given an item in list one, find all the items in list two that are smaller than this item in list one
    i = 0
    bigger_than_lst_one = {}
    smaller_than_lst_one = {}
    while i < len(lst_one):
        for elem in lst_two:
            lst_one_elem = lst_one[i]
            if elem <= lst_one_elem:
                # record what elements in lst two smaller than what elements in lst one 
                save_result_to_dict(smaller_than_lst_one, lst_one_elem, elem)

            else:
                # record what elements in lst two bigger than what elements in lst one 
                save_result_to_dict(bigger_than_lst_one, lst_one_elem, elem)
    
        i = i + 1

    # add items smaller than list A elements
    # Because if an element is smaller than the smallest, than it is also smaller than other items in list one
    for key, value in list(smaller_than_lst_one.items()):
        index_to_insert, new_items = get_index_and_lst_to_insert(new_lst, key, value)
        new_lst[index_to_insert:index_to_insert] = new_items


    # add items bigger than list A elements. 
    # Make sure to add them reversely
    # Because if an element is bigger than the biggest, than it is also bigger than other items in list one
    for key, value in reversed(list(bigger_than_lst_one.items())):
        index_to_insert, new_items = get_index_and_lst_to_insert(new_lst, key, value)
        new_lst = new_lst[:index_to_insert + 1] + new_items + new_lst[index_to_insert + 1:]

    return new_lst


sorted_lst_one = merge_sort(lst_a, lst_b)

print('sorted new list one', sorted_lst_one)

sorted_lst_two = merge_sort(lst_c, lst_d)

print('sorted new list two', sorted_lst_two)

sorted_lst_three = merge_sort(lst_e, lst_f)

print('sorted new list three', sorted_lst_three)

sorted_lst_four = merge_sort(lst_g, lst_h)

print('sorted new list four', sorted_lst_four)