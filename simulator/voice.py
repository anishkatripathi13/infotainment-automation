
def handle_voice_command(command):
    if command.lower() == "play music":
        return "Playing music"
    elif command.lower() == "pause music":
        return "Pausing music"
    else:
        return "Command not recognized"