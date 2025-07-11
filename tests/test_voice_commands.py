from simulator.infotainment_system import InfotainmentSystem

def test_voice_command_play():
    system = InfotainmentSystem()
    response = system.voice_command("play music")
    assert response == "Playing music"

def test_voice_command_invalid():
    system = InfotainmentSystem()
    response = system.voice_command("fly")
    assert response == "Command not recognized"
