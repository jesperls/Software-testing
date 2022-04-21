from source.warehouse import *

def test_create_item():
    wh = warehouse()

    # 1D
    itm = wh.create_item(True)
    for i in itm.risks:
        print(i.name)
    wh.item_risks = [risk("Scanning Risk", "scanning", 100, 0)]

    # 3D
    itm = wh.create_item(True) 
    for i in itm.risks:
        print(i.name)
    
    # 2D
    wh.item_risks = [risk("Handeling Risk", "handeling", 100, 0)]
    itm = wh.create_item(True)
    for i in itm.risks:
        print(i.name)

def test_edit_time_on_shelf():
    wh = warehouse()

    # 8P
    inputs = ["1", "15", "0"]
    wh.edit_time_on_shelf_mock(inputs)

    # 9P
    inputs = ["1", "a", "0"]
    wh.edit_time_on_shelf_mock(inputs)

    # 7P
    inputs = ["0"]
    wh.edit_time_on_shelf_mock(inputs)

    # 10P
    inputs = ["a", "0"]
    wh.edit_time_on_shelf_mock(inputs)

def test_run():
    wh = warehouse()
    wh.create_worker_lst(10, 5, 5, 5)
    wh.create_shelf(100, 5, 5)
    wh.create_arrivals(10)
    for i in range(10):
        wh.arrivals.store.put(wh.create_item(True))

if __name__ == "__main__":
    test_edit_time_on_shelf()
    test_create_item()
    test_run()