"""
tests for calc app
"""

import calculator


class TestCalcApp:
    def test_add(self):
        assert 7 == calculator.add(3, 4)

    def test_subtract(self):
        assert 7 == calculator.subtract(14, 7)
