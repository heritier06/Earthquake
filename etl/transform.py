import datetime

def transform_data(raw_data):
    cleaned = []
    for feature in raw_data["features"]:
        prop = feature["properties"]
        geom = feature["geometry"]
        if not prop["mag"] or not geom or not geom["coordinates"]:
            continue
        cleaned.append({
            "id": feature["id"],
            "magnitude": prop["mag"],
            "place": prop["place"],
            "time": datetime.datetime.utcfromtimestamp(prop["time"] / 1000),
            "coordinates": {
                "type": "Point",
                "coordinates": geom["coordinates"][:2]
            }
        })
    return cleaned