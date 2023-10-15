from src.speech_module.SpeechValidators import ZoneValidator as zv, CommandValidator as cv


class ValidatorZoneAndCommand:

    def __init__(self, commands_info, zones_info):
        self.commands_info = commands_info
        self.zones_info = zones_info

    def Validate(self, zone, command):
        command_validator = cv.CommandValidator(self.commands_info)
        zone_validator = zv.ZoneValidator(self.zones_info)
        if zone_validator.check_zone(zone, command) and command_validator.find_command(command):
            return True
        else:
            return False