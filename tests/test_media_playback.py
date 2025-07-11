from simulator.infotainment_system import InfotainmentSystem

def test_media_playing_with_bluetooth():
    system = InfotainmentSystem()
    system.connect_bluetooth("Phone")
    result = system.play_media("Song A")
    assert result == "Now playing: Song A"
    assert system.media_playing is True

def test_media_stopping():
    system = InfotainmentSystem()
    system.connect_bluetooth("Phone")
    system.play_media("Song A")
    result = system.stop_media()
    assert result == "Media stopped"
    assert system.media_playing is False
