class InfotainmentSystem:
    def __init__(self):
        self.bluetooth_connected = False
        self.media_playing = False
        self.current_song = None
        self.navigation_running = False

    def connect_bluetooth(self, device_name):
        if device_name:
            self.bluetooth_connected = True
            return f"Connected to {device_name}"
        return "No device found"

    def play_media(self, song):
        if self.bluetooth_connected:
            self.media_playing = True
            self.current_song = song
            return f"Now playing: {song}"
        return "Bluetooth not connected"

    def stop_media(self):
        self.media_playing = False
        return "Media stopped"

    def start_navigation(self, destination):
        if destination:
            self.navigation_running = True
            return f"Navigation started to {destination}"
        return "Destination not set"

    def stop_navigation(self):
        self.navigation_running = False
        return "Navigation stopped"

    def recognize_voice_command(self, command):
        commands = {
            "play": "Playing media",
            "stop": "Stopping media",
            "navigate home": "Starting navigation to home"
        }
        return commands.get(command.lower(), "Command not recognized")
