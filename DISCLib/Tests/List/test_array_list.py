import pytest

from DISCLib.ADTs import list as lt

lista = {}


def validate_new_list(list):
    if lista == "NOT_IMPLEMENTED":
        pytest.skip("new_list() Not implemented yet")
        return False
    return True


@pytest.fixture(autouse=True)
def before_each():
    lista = lt.newList(datastructure="ARRAY_LIST")
    validate_new_list(lista)


def test_new_list():
    assert lista["type"] == "ARRAY_LIST"
    assert lista["size"] == 0
    assert lista["elements"] == []


def validate_add_first(list):
    if lista["elements"] == "NOT_IMPLEMENTED":
        pytest.skip("add_first() Not implemented yet")
        return False
    return True


def test_add_first():
    lt.addFirst(lista, 1)

    if validate_add_first(lista):
        lt.addFirst(lista, 2)
        lt.addFirst(lista, 3)

        assert lista["size"] == 3
        assert lista["elements"] == [3, 2, 1]


def test_add_last():
    lt.addLast(lista, 1)

    if lista["elements"] == "NOT_IMPLEMENTED":
        pytest.skip("add_last() Not implemented yet")
    else:
        lt.addLast(lista, 2)
        lt.addLast(lista, 3)

        assert lista["size"] == 3
        assert lista["elements"] == [1, 2, 3]


def test_is_empty():

    is_empty = lt.isEmpty(list)

    if is_empty == "NOT_IMPLEMENTED":
        pytest.skip("is_empty() Not implemented yet")

    assert lt.isEmpty(list) == True

    lt.addFirst(list, 1)

    if validate_add_first(list):
        assert lt.isEmpty(list) == False


def test_get_size():

    list = lt.newList(datastructure="ARRAY_LIST")

    assert lt.size(list) == 0

    lt.addFirst(list, 1)

    assert lt.size(list) == 1


def test_get_first_element():

    list = lt.newList(datastructure="ARRAY_LIST")

    lt.addFirst(list, 1)
    lt.addFirst(list, 2)
    lt.addFirst(list, 3)

    assert lt.firstElement(list) == 3


def test_get_last_element():

    list = lt.newList(datastructure="ARRAY_LIST")

    lt.addFirst(list, 1)
    lt.addFirst(list, 2)
    lt.addFirst(list, 3)

    assert lt.lastElement(list) == 1


def test_get_element():

    list = lt.newList(datastructure="ARRAY_LIST")

    lt.addFirst(list, 1)
    lt.addFirst(list, 2)
    lt.addFirst(list, 3)

    assert lt.getElement(list, 1) == 3
    assert lt.getElement(list, 2) == 2
    assert lt.getElement(list, 3) == 1


def test_remove_first():

    list = lt.newList(datastructure="ARRAY_LIST")

    lt.addFirst(list, 1)
    lt.addFirst(list, 2)
    lt.addFirst(list, 3)

    lt.removeFirst(list)

    assert list["size"] == 2
    assert list["elements"] == [2, 1]


def test_remove_last():

    list = lt.newList(datastructure="ARRAY_LIST")

    lt.addFirst(list, 1)
    lt.addFirst(list, 2)
    lt.addFirst(list, 3)

    lt.removeLast(list)

    assert list["size"] == 2
    assert list["elements"] == [3, 2]


def test_insert_element():

    list = lt.newList(datastructure="ARRAY_LIST")

    lt.addFirst(list, 1)
    lt.addFirst(list, 2)
    lt.addFirst(list, 3)

    lt.insertElement(list, 2, 4)

    assert list["size"] == 4
    assert list["elements"] == [3, 2, 1, 2]


def test_is_present():

    list = lt.newList(datastructure="ARRAY_LIST")

    lt.addFirst(list, 1)
    lt.addFirst(list, 2)
    lt.addFirst(list, 3)

    print(list)

    assert lt.isPresent(list, 1) == 3
    assert lt.isPresent(list, 2) == 2
    assert lt.isPresent(list, 3) == 1
    assert lt.isPresent(list, 4) == 0
