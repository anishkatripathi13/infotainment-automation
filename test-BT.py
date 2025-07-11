from simulator.infotainment_system import InfotainmentSystem

def test_bluetooth_connection():
    system = InfotainmentSystem()
    result = system.connect_bluetooth("Anishka's Phone")
    assert result == "Connected to Anishka's Phone"
