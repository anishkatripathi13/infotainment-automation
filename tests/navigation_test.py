from simulator.infotainment_system import InfotainmentSystem

def test_navigation_start_stop():
    system = InfotainmentSystem()
    start = system.start_navigation("Work")
    stop = system.stop_navigation()
    assert start == "Navigation started to Work"
    assert stop == "Navigation stopped"
