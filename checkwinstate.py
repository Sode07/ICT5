from movement import unit_exists
from turn_handler import getMoneyActual

def voitto(filename, win1X, win1Y, win2x, win2y):
    print("Tilkki")
    print("unit exists", unit_exists(filename, win1X, win1Y))
    print("roobe", getMoneyActual(filename))
    if unit_exists(filename, win1X, win1Y) == 2 and unit_exists(filename, win2x, win2y) == 2 and getMoneyActual(filename) >= 100:
        print("voitit pelin")
        return True
    else:
        return False

def test(filename):
    print("roobe", getMoneyActual(filename))