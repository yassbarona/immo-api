import json
import pandas as pd    
house_json = { 
        "data":{
            "area": 0,
            "property-type":0,
            "rooms-number": 0,
            "zip-code": 0,
            "land-area": 0,
            "garden": None,
            "garden-area": 0,
            "equipped-kitchen": None,
            "full-address": None,
            "swimming-pool": None,
            "furnished": None,
            "open-fire": None,
            "terrace": None,
            "terrace-area": 0,
            "facades-number": 0,
            "building-state": ["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"]
        }
    }   
def preprocess(json):
    df = pd.json_normalize(json["data"])
    return df[['area','property-type','rooms-number','zip-code']] 