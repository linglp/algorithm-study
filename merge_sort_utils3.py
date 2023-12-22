
def find_list_for_elem(elem, list_a, list_b):
    """find what is the list that contains a certain element
    """
    if elem in list_a: 
        # even if element in list a and b, only return list a
        return list_a
    elif elem in list_b:
        return list_b
    else:
        print('this element is not in a or b. something is wrong')
    
def record_smaller_elem(a, b, list_c):
    """push the element that is smaller to list c
    """
    if a <= b:
        list_c.append(a)
    elif b < a:
        list_c.append(b)
    return list_c

def find_comparison_elem_index(a, b, list_a, list_b):
    """Find the index of the element that is smaller, and the index of the element that is bigger
    """
    a_elem_list = find_list_for_elem(a, list_a, list_b)
    b_elem_list = find_list_for_elem(b, list_a, list_b)

    if a <= b: 
        index_smaller_elem = a_elem_list.index(a)
        index_bigger_elem = b_elem_list.index(b)
    else:
        index_smaller_elem = b_elem_list.index(b)
        index_bigger_elem = a_elem_list.index(a)
    return index_smaller_elem, index_bigger_elem

def find_where_smaller_elem(elem_one, elem_two, list_a, list_b):
    """try to find which list the smaller element belongs
    """
    if elem_one >= elem_two:
        # find where elem one belongs since element two is smaller
        return find_list_for_elem(elem_two, list_a, list_b)
    elif elem_one < elem_two:
        # find where elem one belongs since element one is smaller
        return find_list_for_elem(elem_one, list_a, list_b)
    
def find_alternate_list(list_one, list_a, list_b):
    """given one list, return the other list
    """
    if list_one == list_a:
        return list_b
    elif list_one == list_b:
        return list_a

def merge_sort(list_a, list_b):
    # assuming list a and list b are both sorted
    # merge and sort these two lists 
    
    list_c = []
    lst_contain_smaller_elem = list_a
    altnerate_lst = list_b
    smaller_elem_index = 0
    bigger_elem_index = 0
    i = 0

    while len(list_c) < len(list_a) + len(list_b):
        if i == 0:
            # in the beginning, compare the first element in the list
            elem_one = lst_contain_smaller_elem[0]
            elem_two = altnerate_lst[0]
        else:
            try:
                elem_one = lst_contain_smaller_elem[smaller_elem_index + 1]
            except:
                # when list that contain smaller element runs out of bigger element to compare
                # copy the remaining elements from alternate list and be done!
                
                # get all the items remained in alternate list that are bigger
                remained_items = altnerate_lst[bigger_elem_index:]
                list_c = list_c + remained_items
                return list_c


            elem_two = altnerate_lst[bigger_elem_index]

        list_c = record_smaller_elem(elem_one, elem_two, list_c)
        smaller_elem_index, bigger_elem_index = find_comparison_elem_index(elem_one, elem_two, list_a, list_b)
        lst_contain_smaller_elem = find_where_smaller_elem(elem_one, elem_two, list_a, list_b)
        altnerate_lst = find_alternate_list(lst_contain_smaller_elem, list_a, list_b)
        i = i + 1
    return list_c


# testing result
lst_a = [1, 7, 8]
lst_b = [9, 10]
lst_c_expected = [1, 7, 8, 9, 10]
result_one = merge_sort(lst_a, lst_b)
assert result_one == lst_c_expected

lst_a = [1, 2, 3]
lst_b = [9, 10]
lst_c_expected = [1, 2, 3, 9, 10]
result_two = merge_sort(lst_a, lst_b)
assert result_two == lst_c_expected

lst_a = [100, 200, 300]
lst_b = [9, 10]
lst_c_expected = [9, 10, 100, 200, 300]
result_three = merge_sort(lst_a, lst_b)
assert result_three == lst_c_expected

lst_a = [3, 8]
lst_b = [2000, 3000, 5000]
lst_c_expected = [3, 8, 2000, 3000, 5000]
result_four = merge_sort(lst_a, lst_b)
assert result_four == lst_c_expected

lst_a = [1000]
lst_b = [4, 5, 6]
lst_c_expected = [4, 5, 6, 1000]
result_five = merge_sort(lst_a, lst_b)
assert result_five == lst_c_expected

lst_a = [1, 2]
lst_b = [1, 4, 5, 6]
lst_c_expected = [1, 1, 2, 4, 5, 6]
result_six = merge_sort(lst_a, lst_b)
assert result_six == lst_c_expected

lst_a = [1, 2]
lst_b = [1, 2, 4, 5, 6]
lst_c_expected = [1, 1, 2, 2, 4, 5, 6]
result_seven = merge_sort(lst_a, lst_b)
assert result_seven == lst_c_expected