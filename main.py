from SpeechValidators import CommandValidator, ZoneValidator
from SpeechValidators import CommandsInfo
cv = CommandValidator.CommandValidator(CommandsInfo.comms)
print(cv.find_command("включить свет"))
zones = CommandsInfo.zones
print(zones)
zone_info = CommandsInfo.zones
zv = ZoneValidator.ZoneValidator(zone_info)
print(zv.check_zone("far", "построить маршрут для точки"))
