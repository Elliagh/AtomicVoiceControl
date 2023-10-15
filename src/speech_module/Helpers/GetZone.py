

def get_zone(distance):
    nearest_max = 1
    near_max = 10
    far_max = 10 ^ 6
    zone_dict = {1: "nearest", 2: "near", 3: "far", 4: "not defined"}
    if distance <= nearest_max and distance >=0:
        zone = zone_dict[1]
    if distance <= near_max and distance > nearest_max:
        zone = zone_dict[2]
    if distance <= far_max and distance > near_max:
        zone = zone_dict[3]
    if distance > far_max:
        zone = zone_dict[4]
    return zone