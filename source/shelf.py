class shelf:
    def __init__(self, id, store, distance_from_arrivals = 0, distance_from_departure = 0):
        self.id = id
        self.store = store          #container for item objects
        self.distance_from_arrivals = distance_from_arrivals        #distance from arrivals
        self.distance_from_departure = distance_from_departure      #distance from departures
        # self.size = size            #The size of the items allowed on the shelf

    def __len__(self):
        return len(self.store.items)

    def is_empty(self):
        """Returns true if the shelf is empty"""
        if len(self) == 0:
            return True
        return False

    def is_full(self):
        """Returns ture if the shelf is full"""
        if len(self) == self.store.capacity:
            return True
        return False

    def get_item_ids(self):
        """Returns a list of the item ids containd in the shelf"""
        ids = []
        for i in self.store.items:
            ids.append(i.id)
        return ids

    def item_to_be_moved(self, env, worker):
        """Returns an item that can be moved"""
        for item in self.store.items:
            itm = self.store.get()
            if item.when_to_move <= env.now:
                return itm
            self.store.put(itm)
