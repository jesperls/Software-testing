import pandas
import pandas as pd
from source.warehouse import *
from source.risk import *
import json
import re
import os


def import_warehouse(filename):
    """Imports the warehouse from a json file"""
    try:
        with open("Saved Warehouses/" + filename + '.json') as json_file:
            data = json.load(json_file)
            wh = warehouse()
            for i in data["Shelves"][0].values():
                values = re.findall(r'\d+', i)
                wh.create_shelf(int(values[0]), int(values[1]), int(values[2]))
            for i in data["Workers"][0].values():
                values = re.findall(r'\d+', i)
                wh.create_worker_lst(1, int(values[0]), int(values[1]), int(values[2]))
            for i in data["Global Risks"][0].values():
                values = i.split(",")
                wh.global_risks.append(risk(values[0], values[1], float(values[2]), float(values[3])))
            for i in data["Item Risks"][0].values():
                values = i.split(",")
                wh.item_risks.append(risk(values[0], values[1], float(values[2]), float(values[3])))
            arr_dep = list(data["Arrivals"][0].values())
            # print(arr_dep)
            if arr_dep != [[]]:
                wh.create_arrivals(int(arr_dep[0][0]))
                wh.create_departures()
            wh.avg_shelfed = (list(data["AVG Shelfed"][0].values()))[0]
            return wh
    except FileNotFoundError:
        # print("No such file found!")
        return -1


def export_warehouse(wh, filename):
    """Exports the warehouse into a json file"""
    if not os.path.exists("Saved Warehouses"):
        os.makedirs("Saved Warehouses")
    df = pandas.DataFrame()
    shelf_list = []
    for i, shelf in enumerate(wh.shelves):
        shelf_list.append([])
        shelf_list[i].append(shelf.store.capacity)
        shelf_list[i].append(shelf.distance_from_arrivals)
        shelf_list[i].append(shelf.distance_from_departure)
        shelf_list[i] = ",".join(map(str, shelf_list[i]))
    # print(shelf_list)
    shelf_series = pd.Series(shelf_list)
    shelf_series.name = "Shelves"
    df = df.append(shelf_series)

    worker_list = []
    for i, worker in enumerate(wh.workers):
        worker_list.append([])
        worker_list[i].append(worker.scan_time)
        worker_list[i].append(worker.speed)
        worker_list[i].append(worker.item_handeling_time)
        worker_list[i] = ",".join(map(str, worker_list[i]))
    worker_series = pd.Series(worker_list)
    worker_series.name = "Workers"

    df = df.append(worker_series)

    global_risk_list = []
    for i, risk in enumerate(wh.global_risks):
        global_risk_list.append([])
        global_risk_list[i].append(risk.name)
        global_risk_list[i].append(risk.type)
        global_risk_list[i].append(float(risk.probability)*100)
        global_risk_list[i].append(float(risk.magnitude))
        global_risk_list[i] = ",".join(map(str, global_risk_list[i]))
    global_risk_series = pd.Series(global_risk_list)
    global_risk_series.name = "Global Risks"

    df = df.append(global_risk_series)

    item_risk_list = []
    for i, risk in enumerate(wh.item_risks):
        item_risk_list.append([])
        item_risk_list[i].append(risk.name)
        item_risk_list[i].append(risk.type)
        item_risk_list[i].append(float(risk.probability)*100)
        item_risk_list[i].append(float(risk.magnitude))
        item_risk_list[i] = ",".join(map(str, item_risk_list[i]))
    item_risks_series = pd.Series(item_risk_list)
    item_risks_series.name = "Item Risks"

    df = df.append(item_risks_series)

    arrivals_departures = [[]]
    if wh.arrivals is not None:
        arrivals_departures[0].append(wh.arrivals.store.capacity)

    arr_dep_series = pd.Series(arrivals_departures)
    arr_dep_series.name = "Arrivals"

    df = df.append(arr_dep_series)

    df = df.append(pd.Series(data=[wh.avg_shelfed], index=["AVG Shelfed"], name="AVG Shelfed"))

    json = df.apply(lambda x: [x.dropna()], axis=1).T.to_json()

    with open("Saved Warehouses/" + filename + ".json", 'w') as f:
        f.write(json)


if __name__ == "__main__":
    wh = warehouse()
    wh.create_worker_lst(12, 7, 4, 5)
    wh.create_worker_lst(3, 4, 7, 3)
    for i in range(10):
        wh.create_shelf(6, 5, 4)
    wh.create_arrivals(5)
    wh.create_departures(10)
    item_risks = [["Fragile", "moving", 0.15, 20]]  # name, itype, probability, magnitude (seconds)
    for i in item_risks:
        wh.item_risks.append(risk(i[0], i[1], i[2], i[3]))

    global_risks = [["Missplace", "handeling", 0.1, 10], ["Scanning Error", "scanning", 0.1, 5]]
    for i in global_risks:
        wh.global_risks.append(risk(i[0], i[1], i[2], i[3]))

    wh.time_modifier = 2

    export_warehouse(wh, "test")

    wh2 = import_warehouse("test")

    print("test")
