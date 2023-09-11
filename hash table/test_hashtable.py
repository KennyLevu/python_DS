# test_hashtable.py
from hashtable import HashTable, BLANK
import pytest

def test_should_always_pass():
    assert 2 + 2 == 4, "This is just a dummy test"

def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None

def test_should_report_capcity():
    assert len(HashTable(capacity=100)) == 100

def test_should_create_empty_value_slots():
    # Given
    expected_values = [None, None, None]
    hash_table = HashTable(capacity=3)

    # When
    actual_values = hash_table.values

    # Then
    assert actual_values == expected_values

# @pytest.mark.skip
def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=100)

    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True
    
    assert "hello" in hash_table.values
    assert 37 in hash_table.values
    assert True in hash_table.values

    assert len(hash_table) == 100

def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=100).values

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [BLANK, BLANK, BLANK]

def test_should_insert_none_value():
    hash_table = HashTable(capacity=100)
    hash_table["key"] = None
    print(hash_table)
    assert None in hash_table.values