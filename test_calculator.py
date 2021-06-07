"""
tests for calc app
"""

import calculator


class TestCalcApp:
    def test_add(self):
        assert 7 == calculator.add(3, 4)

    def test_subtract(self):
        assert 7 == calculator.subtract(14, 7)

    def test_multiply(self):
        assert 20 == calculator.multiply(4, 5)

    def test_divide(self):
        assert 7 == calculator.divide(28, 4)
