


def ConverterSTringToCoords(string:str):
    latlon = string.split(" ")
    return (float(latlon[0]), float(latlon[1]))
