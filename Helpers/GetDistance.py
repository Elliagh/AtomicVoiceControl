

from geopy.distance import geodesic as GD

def get_distance(user, car):
    return GD(user,car).m