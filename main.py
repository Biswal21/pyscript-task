list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.

    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    merged_list = []
    dict_2 = {item["id"]: item for item in list_2}
    for item in list_1:
        merged_item = item.copy()
        other_item = dict_2.get(item["id"])
        if other_item:
            merged_item.update(other_item)
        merged_list.append(merged_item)
    return merged_list


list_3 = merge_lists(list_1, list_2)
print("Merged List: ", list_3)
