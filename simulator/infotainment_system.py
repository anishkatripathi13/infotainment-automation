from simulator.bluetooth import connect_device
from simulator.media import play_music, pause_music, stop_music
from simulator.navigation import start_navigation
from simulator.voice import handle_voice_command

class InfotainmentSystem:
    def __init__(self):
        self.connected_device = None

    def connect_bluetooth(self, device):
        self.connected_device = device
        return connect_device(device)

    def play(self):
        return play_music()

    def pause(self):
        return pause_music()

    def stop(self):
        return stop_music()

    def navigate_to(self, destination):
        return start_navigation(destination)

    def voice_command(self, command):
        return handle_voice_command(command)