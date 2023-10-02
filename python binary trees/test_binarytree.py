# test_binarytree.py
from binarytree import BinaryTree
import pytest

def test_should_always_pass():
    assert 2 + 2 == 4, "This is just a dummy test"

def test_should_create_binarytree():
    assert BinaryTree(1) is not None

def test_should_add_node_binarytree():
