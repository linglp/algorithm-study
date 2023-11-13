names = [
    "Adam",
    [
        "Bob", 
        "Alfred"

    ],
    "Vishwaas",
    [
        "Yoshikawa", 
        "Yamamoto"

    ],
]

def count_leaf_items(item_list):
    num_leaf_items = 0
    for i in item_list:
        if isinstance(i, list):
            num_leaf_items = count_leaf_items(i)
        else:
            print('counting', i)
            num_leaf_items += 1
    return num_leaf_items

num_leaf_items = count_leaf_items(names)
print(num_leaf_items)