"""
@author Joe

This file contains some pretty functions
"""


def get_top_k_indexes_of_list(target_list, k, is_max=True):
    """
    get the top k indexes of elements in list

    Example:
    Problem: I have a list say a = [5,3,1,4,10],
            and I need to get a index of top two values of the list viz 5 and 10.
            Is there a one-liner that python offers for such a case?
    Usage: get_top_k_indexes_of_list(target_list=a, k=2, is_max=True)

    link: https://stackoverflow.com/questions/13070461/get-index-of-the-top-n-values-of-a-list-in-python

    :param target_list: target list
    :param k: the number of indexes
    :param is_max: True means max else False means min
    :return: a list of indexes
    """
    indexes = sorted(range(len(target_list)), key=lambda i: target_list[i], reverse=is_max)[:k]
    return indexes


def get_elements_from_list(target_list, indexes):
    """
    get elements from target_list by indexes
    :param target_list: target list
    :param indexes: a list of indexes
    :return: a list of elements
    """
    elements = [target_list[i] for i in indexes]
    return elements

