path_command_file = "Commands.txt"

exist_commands = []
with open(r"SpeechValidators/Commands.txt", encoding="utf-8") as file_commands:
    for line in file_commands.readlines():
        exist_commands.append(line.rstrip('\n'))

comms = exist_commands

zones = {}

with open(r"SpeechValidators/Zones.txt", encoding="utf-8") as file_zones:
    i = 0
    for line in file_zones:
        zones[comms[i]] = line.rstrip('\n').split(" ")
        i = i + 1
