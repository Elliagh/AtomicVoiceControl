import Recognizer as r

def check_command(command):
    with open("Commands.txt", encoding="utf-8") as file_commands:
        for line in file_commands.readlines():
            line  = line.rstrip('\n')
            if line == command:
                return True
                break
        return False


rc = r.Recognizer()

text = rc.get_text()
print(check_command(text))


