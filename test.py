import pytest


# множества
def test_set_clear():
    a = {1, 2, 3}
    a.clear()
    assert a == set()


@pytest.mark.parametrize('i', ['str', True, 5, None, tuple('hello')])
def test_set_add(i):
    a = set()
    a.add(i)
    assert i in a


def test_set_intersection():
    a = {i for i in range(1, 4)}
    b = {i for i in range(3, 5)}
    assert a.intersection(b) == {3}


# словари
# негативный тест
def test_dict_keys():
    a = {1: 'a', 2: 'b', 3: 'c'}
    try:
        a[[1, 2]] = 'lst'
    except TypeError:
        pass


def test_dict_del():
    a = {1: 'a', 2: 'b', 3: 'c'}
    del a[1]
    assert 'a' not in a.values()


def test_dict_clear():
    i = {1: 'a', 2: 'b', 3: 'c'}
    i.clear()
    assert i == {}
