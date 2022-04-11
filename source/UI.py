class UI:
    def UI(self, id, modifiers):

        if id == 0:
            return """
Warehouse Sim 1.0 

1. Create Warehouse
2. Load/Save Warehouse
3. View/Edit Warehouse
4. Simulate
0. Exit


                """
        elif id == 1:
            return """
Create Warehouse:

1. Create workers
2. Create arrivals
3. Create shelf
4. Manage items
5. Average item time on shelves
0. Back


                """
        elif id == 2:
            return """
Create workers:

1. Create multiple workers
2. Create single worker
0. Back     
            
                
                """

        elif id == 3:
            return"""

Create multiple workers:

1. Amount: {0}
2. Scan time: {1}s
3. Walking Speed: {2} m/s
4. Item handeling time: {3}s
5. Create.
0. Back
                
                
                """.format(modifiers[0], modifiers[1], modifiers[2], modifiers[3])

        elif id == 4:
            return"""
Create single worker

1. Scan time: {0}s
2. Walking Speed: {1} m/s
3. Item handeling time: {2}s
4. Create.
0. Back


                """.format(modifiers[0], modifiers[1], modifiers[2])

        elif id == 5:
            return """
Create Arrivals

1. Arrivals capacity: {0}
2. Create
0. Back


            """.format(modifiers[0])
        elif id == 6:
            return """

Create Shelf

1. Shelf capacity: {0} items
2. Distance from arrivals: {1}m
3. Distance from departures: {2}m
4. Create.
0. Back


                """.format(modifiers[0], modifiers[1], modifiers[2])

        elif id == 7:
            return """
Manage Items

1. Create scanning risks
2. Create moving risks
3. Create handeling risks
0. Back


                    """

        elif id == 8:
            return """
Create {0}

1. Name: {1}
2. Probability (1-100%): {2}
3. Time penalty: {3} Seconds
4. Create
0. Back.



                    """.format(modifiers[0], modifiers[1], modifiers[2], modifiers[3])

        elif id == 9:
            return"""
Average item shelf time.

1. Set shelf time: {0}s
0. Back


                    """.format(modifiers[0])
        elif id == 10:
            return """
Load/Save Warehouse

1. Load Warehouse
2. Save Warehouse
0. Back


                """
        elif id == 11:
            return """
Simulate average package time on shelves.

1. Seconds to simulate: {0}
2. Item arrival frequency: Every {1} Second
3. Simulate
0. Back


                """.format(modifiers[0], modifiers[1])
        elif id == 12:
            return """
View/Edit Warehouse
1. View/Edit workers
2. View/Edit arrivals
3. View/Edit shelf
4. View/Edit item risk
5. View/Edit item time on shelves
0. Back


                """
        elif id == 13:
            return"""
Edit worker

1. Scan time: {0}s
2. Walking Speed: {1} m/s
3. Item handeling time: {2}s
4. Remove
0. Back


                """.format(modifiers[0],modifiers[1], modifiers[2])
        elif id == 14:
            return """
Edit Shelf

1. Shelf capacity: {0} items
2. Distance from arrivals: {1}m
3. Distance from departures: {2}m
4. Remove
0. Back


                """.format(modifiers[0],modifiers[1], modifiers[2])
        elif id == 15:
            return """
Edit Risk

1. Name: {0}
2. Probability (1-100%): {1}
3. Time penalty: {2} Seconds
4. Remove
0. Back.


                """.format(modifiers[0],modifiers[1], modifiers[2])














