from simulator.infotainment_system import InfotainmentSystem

def test_media_playing_with_bluetooth():
    system = InfotainmentSystem()
    system.connect_bluetooth("Phone")
    result = system.play()
    assert result == "Music started"

def test_media_stopping():
    system = InfotainmentSystem()
    system.connect_bluetooth("Phone")
    system.play()
    result = system.stop()
    assert result == "Music stopped"
