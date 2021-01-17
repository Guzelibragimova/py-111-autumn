"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
import networkx as nx


bts = {}

# bts = {
#     'key': 0,
#     'value': 123,
#     'left': {
#         'key': 1,
#         'value': [1, 4],
#
#         ...},
#     'right':{...}

def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    global bts
    def insert_(subtree: dict):
        if not subtree:
            "Создание нового потомка листа"
            subtree['key'] = key
            subtree['value'] = value
            subtree['left'] = {}
            subtree['right'] = {}
        else:
            dst_subtree = insert_(subtree['right']) if key >= subtree['key'] else subtree['left']
            insert_(dst_subtree)
        insert_(bts)
    # if not bts:
    #     bts['key'] = key
    #     bts['value'] = value
    #     bts['left'] = {}
    #     bts['right'] = {}
    # else:
    #     new_subtree = bts['right'] if key >= bts['key'] else bts['left']
    #     insert(new_subtree)
    # insert(bts)



        print(key, value)
        return None


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    print(key)
    return None


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    print(key)
    return None


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    global bts
    bts.clear
    return None
