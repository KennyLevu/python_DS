# test_binarytree.py
from mergesort import merge_sort
import pytest


def test_should_always_pass():
    assert 2 + 2 == 4, "This is just a dummy test"

def test_sort_num_list():
    list = [10, 7, 7, 8, 0, -7, 100, 50, 49]
    solution = [-7, 0, 7, 7, 8, 10, 49, 50, 100]
    assert merge_sort(list) == solution
