# Forked from https://github.com/ds5110/stinky2/blob/main/src/get_smc_data.py

import csv
import datetime
import math
import time
import requests

URL = "https://api.smellpittsburgh.org/api/v2/smell_reports"

outfile = "data/smc_data.csv"

PARAMS = {
    "format": "json",
    "zipcodes": "04101,04102,04106,04107,04103,04108,04124",
    "start_time": "1577836800",  # Jan 1 2020 12:00 AM
    "end_time": int(time.time()),  # right meow
    "timezone_string": "America%2FNew_York"
}

# Addresses found in Maine DEP report
# https://www.protectsouthportland.com/_files/ugd/6281f2_699328196df94c75a61f58fd4824abc2.pdf

# Lat long found using https://www.latlong.net/convert-address-to-lat-long.html

tank_coord_deg = {
    "sprague": (43.637210, -70.286400),
    "portland_pipeline": (43.629500, -70.271290),
    "south_portland_terminal": (43.635930, -70.285290),
    "gulf_oil": (43.650240, -70.239670),
    "global": (43.634410, -70.284430),
    "citgo": (43.637009, -70.267303)
}

with open(outfile, "w") as data_file:
    try:
        resp = requests.get(url=URL, params=PARAMS)
    except Exception as exc:
        print(f"An exception occurred on GET: {exc}")
        raise
    csv_writer = csv.writer(data_file)

    raw_smc_data = resp.json()

    filtered_smc_data = []

    for complaint in raw_smc_data:
        # filter out data with no zip code or a zip code not asked for
        if complaint["zipcode"] and len(complaint["zipcode"]) <= 5 and complaint["zipcode"] in PARAMS["zipcodes"].split(","):
            # parse raw time
            complaint["epoch time"] = complaint["observed_at"]
            # parse python local time
            complaint["date & time"] = time.ctime(complaint["observed_at"])
            # parse datetime string
            complaint["date"] = datetime.datetime.fromtimestamp(
                complaint["observed_at"]).strftime('%x')
            complaint.pop("observed_at")
            # calculate distances to possible sources
            lat1 = complaint["latitude"] / (180 / math.pi)
            lon1 = complaint["longitude"] / (180 / math.pi)
            for tank, coord in tank_coord_deg.items():
                lat2 = float(coord[0]) / (180 / math.pi)
                lon2 = float(coord[1]) / (180 / math.pi)
                dist = 3963 * math.acos((math.sin(lat1)*math.sin(lat2)) +
                                        math.cos(lat1)*math.cos(lat2)*math.cos(lon2 - lon1))
                complaint[tank + "_miles"] = dist

            filtered_smc_data.append(complaint)

    csv_writer.writerow(filtered_smc_data[0].keys())

    for row in filtered_smc_data:
        csv_writer.writerow(row.values())
