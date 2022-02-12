import random
from lotto_game import insert_space_func, create_card, card_name


def test_insert_space_func_one():
    name = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    insert_space_func(name)
    assert len(name[0]) == 9


def test_insert_space_func_two():
    name1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    insert_space_func(name1)
    assert len(name1[1]) == 9


def test_insert_space_func_three():
    name2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    insert_space_func(name2)
    assert len(name2[2]) == 9



