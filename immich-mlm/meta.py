import datetime
import math
import numpy as np

def distancehaversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlon/2)**2 + math.cos(lon1) * math.cos(lon2) * math.sin(dlat/2)**2
    c = 2 * np.arcsin(math.sqrt(a))
    km = 6367 * c
    return km


def distance_to_tag(km):
    tag = "GEO/Unknown"
    if km < 0.1:
        tag = "GEO/Home"
    elif km < 4.0:
        tag = "GEO/Local"
    elif km < 40.0:
        tag = "GEO/Metro"
    else:
        tag = "GEO/Away"
    return tag



def meta_geo_distance_from_home():
    pass


def meta_device_type():
    pass


def meta_media_key():
    pass


def meta_birthday():
    pass
