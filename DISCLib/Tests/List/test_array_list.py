from DISCLib.ADTs import list as lt

def test_new_list():

    list = lt.newList(datastructure="ARRAY_LIST")

    print(list)

    assert list["type"] == "ARRAY_LIST"
    assert list["size"] == 0
    assert list["elements"] == []

def test_add_first():

    list = lt.newList(datastructure="ARRAY_LIST")

    lt.addFirst(list, 1)
    lt.addFirst(list, 2)
    lt.addFirst(list, 3)

    print(list)

    assert list["size"] == 3
    assert list["elements"] == [3, 2, 1]

def test_add_last():
    
        list = lt.newList(datastructure="ARRAY_LIST")
    
        lt.addLast(list, 1)
        lt.addLast(list, 2)
        lt.addLast(list, 3)
    
        print(list)
    
        assert list["size"] == 3
        assert list["elements"] == [1, 2, 3]

def test_is_empty():

    list = lt.newList(datastructure="ARRAY_LIST")

    assert lt.isEmpty(list) == True

    lt.addFirst(list, 1)

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