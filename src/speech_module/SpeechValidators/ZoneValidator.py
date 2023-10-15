

class ZoneValidator:

    def __init__(self, dictionary_zones):
        self.dictionary_zones = dictionary_zones


    def check_zone(self, zone, command):
        zones = self.dictionary_zones[command]
        if zone in zones:
            return True
        else:
            return False
