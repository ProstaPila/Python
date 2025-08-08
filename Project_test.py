from Project import temperatureConversionLogic
import pytest

def test_temperatureConversionLogic():
    assert temperatureConversionLogic("C","F",20) == 68, "Should be 68F"
