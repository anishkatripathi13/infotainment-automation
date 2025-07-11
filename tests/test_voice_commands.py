from simulator.infotainment_system import InfotainmentSystem

def test_voice_command_play():
    system = InfotainmentSystem()
    response = system.recognize_voice_command("play")
    assert response == "Playing media"

def test_voice_command_invalid():
    system = InfotainmentSystem()
    response = system.recognize_voice_command("fly")
    assert response == "Command not recognized"
