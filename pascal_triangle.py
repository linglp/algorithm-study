# Write a function which implements the Pascal's triangle:

# 1
# 1     1
# 1     2     1
# 1     3     3     1
# 1     4     6     4     1
# 1     5     10    10     5    1


def return_number_for_next_layer(layer_list):
    """based on list of number in the previvous layer, return the numbers needed for the next layer. 
    For example, if previous layer = [1, 2, 1], then the output of this function would return [3, 3] which are the two numbers
    needed in the fourth layer
    """
    if len(layer_list)== 1:
        return [1, 1]
    else:
        items_to_return = []
        for i in range(len(layer_list)):
            if i+1 < len(layer_list):
                items_to_return.append(layer_list[i] + layer_list[i+1])
        return items_to_return


def pascal_triangle_find_layer(layer_number):
    # find a given layer in pascal triangle
    if layer_number == 1:
        return [1]
    elif layer_number == 2:
        return [1, 1]
    else:
        if layer_number > 0:
            # find the bottom layer using recursive strategy
            previous_layer = pascal_triangle_find_layer(layer_number-1)
            results_from_previous_layer = return_number_for_next_layer(previous_layer)
            # add 1 as the first and last item
            results_from_previous_layer.append(1)
            results_from_previous_layer.insert(0, 1)
            return results_from_previous_layer
            


the_third_layer = pascal_triangle_find_layer(3)
#print('the third layer', the_third_layer)



def build_pascal_triangle(num_layer):
    # build pascal triangle based on the number of layers
    if num_layer == 1:
        return [[1]]
    elif num_layer == 2: 
        return [[1], [1, 1]]
    else: 
        if num_layer > 0:
            # build pascal triangle with n - 1 layer
            previous_triangle = build_pascal_triangle(num_layer - 1)
            next_layer = return_number_for_next_layer(previous_triangle[-1])
            # add 1 as the first and last item
            next_layer.append(1)
            next_layer.insert(0, 1)
            new_triangle = previous_triangle + [next_layer]
            return new_triangle

pascal_triangle = build_pascal_triangle(6)
print('pascal_triangle', pascal_triangle)