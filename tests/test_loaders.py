import pytest

from loaders import load_data
from models import Operation


@pytest.fixture
def result():
    result = load_data('test.json')
    return result


def test_load_data(result):
    assert type(result) == list
    assert len(result) == 3
    assert isinstance(result[0], Operation) == True
    assert repr(result[0]) == """26.08.2019 Перевод организации
Maestro 1596 83** **** 5199 -> Счет **9589
31957.58 руб. 
"""


def test_load_data_false():
    res = load_data('false.json')
    assert type(res) == list
    assert len(res) == 0
    assert res == []
