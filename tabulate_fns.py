from tabulate import tabulate

def make_array_for_tabulating(keys, json_object_array):
    tabulate_ary = []
    id = 0
    for json_obj in json_object_array:
        tabulate_item = []
        tabulate_item.append(id)
        id += 1
        for key in keys:
            tabulate_item.append(json_obj[key])
        tabulate_ary.append(tabulate_item)
    return tabulate_ary

def print_tabulating_array(tabulating_array, headers):
    print(tabulate(tabulating_array, headers=headers))