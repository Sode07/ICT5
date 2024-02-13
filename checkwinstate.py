from movement import unit_exists
from turn_handler import getMoneyActual

def voitto(filename, winX, winY):
    print("unit exists", unit_exists(filename, winX, winY))
    print("roobe", getMoneyActual(filename))
    if unit_exists(filename, winX, winY) == 2 and getMoneyActual(filename) >= 100:
        print("voitit pelin")
        return True
    else:
        return False

def test(filename):
    print("roobe", getMoneyActual(filename))