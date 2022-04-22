from source.warehouse import *

def test_create_item():
    wh = warehouse()

    # 1D
    print("Test: (id: 1D): ", end="")
    itm = wh.create_item(True)
    for i in itm.risks:
        print(i.name)
    wh.item_risks = [risk("Scanning Risk", "scanning", 100, 0)]

    # 3D
    print("Test: (id: 1D): ", end="")
    itm = wh.create_item(True) 
    for i in itm.risks:
        print(i.name)
    
    # 2D
    print("Test: (id: 2D): ", end="")
    wh.item_risks = [risk("Handeling Risk", "handeling", 100, 0)]
    itm = wh.create_item(True)
    for i in itm.risks:
        print(i.name)

def test_edit_time_on_shelf():
    wh = warehouse()

    # 8P
    print("Test: (id: 8P): ", end="")
    inputs = ["1", "15", "0"]
    wh.edit_time_on_shelf_mock(inputs)

    # 9P
    print("Test: (id: 9P): ", end="")
    inputs = ["1", "a", "0"]
    wh.edit_time_on_shelf_mock(inputs)

    # 7P
    print("Test: (id: 7P): ", end="")
    inputs = ["0"]
    wh.edit_time_on_shelf_mock(inputs)

    # 10P
    print("Test: (id: 10P): ", end="")
    inputs = ["a", "0"]
    wh.edit_time_on_shelf_mock(inputs)

def test_run():
    print("Testing warehouse.run(): \n")

    # 6S & 7D
    print("Test: (id: 6S, 7D): ", end="")
    wh = warehouse()
    wh.create_worker_lst(1, 5, 5, 5)
    wh.create_shelf(1, 5, 5)
    wh.create_arrivals(1)
    wh.create_departures()
    for i in range(1):
        wh.arrivals.store.put(wh.create_item(True))
    wh.simulate_mock(10, False, 1, "A-B-C-D")

    # 7S & 9D
    print("Test: (id: 7S, 9D): ", end="")
    wh = warehouse()
    wh.create_shelf(1, 5, 5)
    wh.create_arrivals(1)
    wh.create_departures()
    for i in range(1):
        wh.arrivals.store.put(wh.create_item(True))
    wh.simulate_mock(10, False, 1, "A-B-G-H-I-J")

    # 8S & 13D
    print("Test: (id: 8S, 13D): ", end="")
    wh = warehouse()
    wh.create_worker_lst(1, 5, 5, 5)
    wh.create_shelf(1, 5, 5)
    wh.create_arrivals(1)
    wh.create_departures()
    for i in range(1):
        wh.arrivals.store.put(wh.create_item(True))
    for s in wh.shelves:
        s.store.put(wh.create_item(testing=True))
    wh.simulate_mock(10, False, 1, "A-B-G-H-M-N-O-P-Q-S")

    # 9S & 15D
    print("Test: (id: 9S, 15D): ", end="")
    wh = warehouse()
    wh.create_worker_lst(1, 5, 5, 5)
    wh.create_shelf(10, 5, 5)
    wh.create_arrivals(1)
    wh.create_departures()
    for i in range(1):
        wh.arrivals.store.put(wh.create_item(True))
    wh.simulate_mock(10, False, 2, "A-B-G-H-M-N-V-W")

    # 10S & 11D
    print("Test: (id: 10S, 11D): ", end="")
    wh = warehouse()
    wh.create_departures()
    wh.simulate_mock(10, False, 2, "A-B-G-H-M-Z")

    # Done

    # 8D
    print("Test: (id: 8D): ", end="")
    wh = warehouse()
    wh.create_worker_lst(1, 5, 5, 5)
    wh.workers[0]._is_waiting = False
    wh.create_departures()
    wh.simulate_mock(10, False, 1, "A-B-C-F")

    # 10D
    print("Test: (id: 10D): ", end="")
    wh = warehouse()
    wh.create_shelf(0, 5, 5)
    wh.create_departures()
    wh.simulate_mock(10, False, 2, "A-B-G-H-I-L")

    # 12D
    print("Test: (id: 12D): ", end="")
    wh = warehouse()
    wh.create_worker_lst(1, 5, 5, 5)
    wh.create_arrivals(1)
    wh.create_departures()
    for i in range(1):
        wh.arrivals.store.put(wh.create_item(True))
    wh.simulate_mock(10, False, 1, "A-B-G-H-M-N-O-U")

    # 14D
    print("Test: (id: 14D): ", end="")
    wh = warehouse()
    wh.create_worker_lst(1, 5, 5, 5)
    wh.create_shelf(1, 5, 5)
    wh.create_arrivals(1)
    wh.create_departures()
    for i in range(1):
        wh.arrivals.store.put(wh.create_item(True))
    wh.simulate_mock(10, False, 1, "A-B-G-H-M-N-O-P-Q-R")

    # 16D
    print("Test: (id: 16D): ", end="")
    wh = warehouse()
    wh.create_worker_lst(1, 5, 5, 5)
    wh.create_arrivals(1)
    wh.create_departures()
    for i in range(1):
        wh.arrivals.store.put(wh.create_item(True))
    wh.simulate_mock(10, False, 2, "A-B-G-H-M-N-V-Y")

if __name__ == "__main__":
    test_edit_time_on_shelf()
    test_create_item()
    test_run()