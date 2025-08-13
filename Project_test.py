from TemperatureConversion import fromCtoF, fromCtoK , fromKtoC, fromKtoF, fromFtoC, fromFtoK
from pytest import approx

def test_fromCtoF():
    assert fromCtoF(10) == 50, "Should be 50"

def test_fromCtoK():
    assert fromCtoK(-273.15) == 0, "Its absolute 0"

def test_fromKtoC():
    assert fromKtoC(298.15) == 25, "Should be 25"

def test_fromKtoF():
    assert fromKtoF(340) == approx(152.3, abs=1e-1), "Should be 152.3"

def test_fromFtoC():
    assert fromFtoC(77) == 25, "Should be 25"

def test_fromFtoK():
    assert fromFtoK(150) == approx(338.7, abs=1e-1), "Should be 338.7"