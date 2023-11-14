mock_tree_structure = [
    {
    "Tea": ["Bubble tea", "Black tea"]
    }, 
    {
    "Bubble tea": ["Taro milk tea", "Oolong bubble tea"]
    }, 
    {
    "Black tea": ["Premium Black tea"]
    }, 
    {
    "Taro milk tea": ["Taro milk tea with pearls"]
    }
]

def find_the_right_dict(node_name):
    dict_to_return = None
    for dict_to_return in mock_tree_structure:
        if node_name in dict_to_return:
            break
    return dict_to_return
            

def find_children(node_name):
    # if a node is in the tree
    all_children = []
    # find the dictionary that contains this node if any 
    target_dict = find_the_right_dict(node_name)
    if target_dict is not None: 
        try: 
            children = target_dict[node_name]
            if len(children) > 1:
                for i in children:
                    all_children.append(i)
                    print(f'{i} gets added')
                    all_children = all_children + find_children(i)
                    print(f'{children} get added')
            else: 
                all_children.append(children[0])
        except:
            # if an element doesn't have children to return
            print(f"{node_name} does not have any children")
    else: 
        all_children = [node_name]
    return all_children

children = find_children("Bubble tea")
print(f'children of bubble tea: {children}')

# children = find_children("Black tea")
# print(f'children of black tea tea: {children}')

# children = find_children("Tea")
# print(f'children of tea: {children}')