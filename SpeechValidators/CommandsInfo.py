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
zero_paths = []
dict_command_path = {}
with open(r"SpeechValidators/CommandsPath.txt", encoding="utf-8") as file_paths:
    i = 0
    for line in file_paths.readlines():
        path = zero_paths.append(line.rstrip('\n'))
        dict_command_path[comms[i]] = path
        i = i + 1

paths = zero_paths