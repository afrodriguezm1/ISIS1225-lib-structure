from DISCLib.Tests.utils import handle_not_implemented

from DISCLib.ADTs import list as lt


def setup_tests():
    return lt.newList(datastructure="ARRAY_LIST")


@handle_not_implemented
def test_new_list():
    lista = setup_tests()
    assert lista["type"] == "ARRAY_LIST"
    assert lista["size"] == 0
    assert lista["elements"] == []


@handle_not_implemented
def test_add_first():
    lista = setup_tests()

    lt.addFirst(lista, 1)
    lt.addFirst(lista, 2)
    lt.addFirst(lista, 3)

    assert lista["size"] == 3
    assert lista["elements"] == [3, 2, 1]


@handle_not_implemented
def test_add_last():
    lista = setup_tests()

    lt.addLast(lista, 1)
    lt.addLast(lista, 2)
    lt.addLast(lista, 3)

    assert lista["size"] == 3
    assert lista["elements"] == [1, 2, 3]


@handle_not_implemented
def test_is_empty():
    lista = setup_tests()

    assert lt.isEmpty(lista) == True

    lt.addFirst(lista, 1)
    assert lt.isEmpty(lista) == False


@handle_not_implemented
def test_get_size():
    lista = setup_tests()

    assert lt.size(lista) == 0

    lt.addFirst(lista, 1)

    assert lt.size(lista) == 1


@handle_not_implemented
def test_get_first_element():

    lista = setup_tests()

    lt.addFirst(lista, 1)
    lt.addFirst(lista, 2)
    lt.addFirst(lista, 3)
    assert lt.firstElement(lista) == 3


@handle_not_implemented
def test_get_last_element():

    lista = setup_tests()

    lt.addFirst(lista, 1)

    lt.addFirst(lista, 2)
    lt.addFirst(lista, 3)
    assert lt.lastElement(lista) == 1


@handle_not_implemented
def test_get_element():

    lista = setup_tests()

    lt.addFirst(lista, 1)
    lt.addFirst(lista, 2)
    lt.addFirst(lista, 3)

    assert lt.getElement(lista, 1) == 3
    assert lt.getElement(lista, 2) == 2
    assert lt.getElement(lista, 3) == 1


@handle_not_implemented
def test_remove_first():
    lista = setup_tests()

    lt.addFirst(lista, 1)
    lt.addFirst(lista, 2)
    lt.addFirst(lista, 3)

    lt.removeFirst(lista)

    assert lista["size"] == 2
    assert lista["elements"] == [2, 1]


@handle_not_implemented
def test_remove_last():
    lista = setup_tests()

    lt.addFirst(lista, 1)
    lt.addFirst(lista, 2)
    lt.addFirst(lista, 3)

    lt.removeLast(lista)

    assert lista["size"] == 2
    assert lista["elements"] == [3, 2]


@handle_not_implemented
def test_insert_element():
    lista = setup_tests()

    lt.addFirst(lista, 1)
    lt.addFirst(lista, 2)
    lt.addFirst(lista, 3)

    lt.insertElement(lista, 2, 4)

    assert lista["size"] == 4
    assert lista["elements"] == [3, 2, 1, 2]


@handle_not_implemented
def test_is_present():
    lista = setup_tests()

    lt.addFirst(lista, 1)
    lt.addFirst(lista, 2)
    lt.addFirst(lista, 3)

    assert lt.isPresent(lista, 1) == 3
    assert lt.isPresent(lista, 2) == 2
    assert lt.isPresent(lista, 3) == 1
    assert lt.isPresent(lista, 4) == 0
