
import requests
import json
from math import cos, sin, radians

def ra_dec_to_xyz(ra_deg, dec_deg, distance_ly):
    ra = radians(ra_deg)
    dec = radians(dec_deg)
    x = distance_ly * cos(dec) * cos(ra)
    y = distance_ly * cos(dec) * sin(ra)
    z = distance_ly * sin(dec)
    return x, y, z

def fetch_donki():
    url = "https://kauai.ccmc.gsfc.nasa.gov/DONKI/WS/get/FLR"
    params = {
        'startDate': '2025-01-01',
        'endDate': '2025-12-31',
        'api_key': 'DEMO_KEY'
    }
    response = requests.get(url, params=params)
    data = response.json()

    events = []
    for flare in data:
        ra, dec = 90, 0  # placeholder
        x, y, z = ra_dec_to_xyz(ra, dec, 100)
        events.append({
            "name": flare.get("flrID", "unknown"),
            "x": x, "y": y, "z": z,
            "type": "solar_flare"
        })

    with open("data/events.json", "w") as f:
        json.dump(events, f, indent=2)

if __name__ == "__main__":
    fetch_donki()
