# compare item from list a and list b
# whatever that is smaller, record that one
# for the one that is bigger, continue to compare that item with the next element in the other list


def find_list_for_elem(elem, list_a, list_b):
    """find what is the list that contains a certain element
    """
    if elem in list_a and elem in list_b: 
        print('this element exists in both list a and list b')
    elif elem in list_a and elem not in list_b: 
        return list_a
    elif elem in list_b and elem not in list_a: 
        return list_b


def record_smaller_elem(a, b, list_c):
    if a < b:
        list_c.append(a)
    elif b < a:
        list_c.append(b)
    print('what list_c looks like', list_c)
    return list_c

def find_comparison_elem_index(a, b, list_a, list_b):
    a_elem_list = find_list_for_elem(a, list_a, list_b)
    b_elem_list = find_list_for_elem(b, list_a, list_b)

    if a < b: 
        index_smaller_elem = a_elem_list.index(a)
        index_bigger_elem = b_elem_list.index(b)
    elif a > b:
        index_smaller_elem = b_elem_list.index(b)
        index_bigger_elem = a_elem_list.index(a)
    return index_smaller_elem, index_bigger_elem

def find_where_smaller_elem(elem_one, elem_two, list_a, list_b):
    """try to find where the smaller element belongs
    """
    if elem_one > elem_two:
        # find where elem one belongs since element two is smaller
        return find_list_for_elem(elem_two, list_a, list_b)
    elif elem_one < elem_two:
        # find where elem one belongs since element one is smaller
        return find_list_for_elem(elem_one, list_a, list_b)
    
def find_alternate_list(list_one, list_a, list_b):
    if list_one == list_a:
        return list_b
    elif list_one == list_b:
        return list_a

# another way to deal with merging 
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




lst_a = [1, 3, 100]
lst_b = [10, 1000, 2000]
list_c = merge_sort(lst_a, lst_b)
assert list_c == [1, 3, 10, 100, 1000, 2000]

