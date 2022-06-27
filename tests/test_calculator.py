#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_Calculator.py
@Time    :   2022/06/27 19:12:58
@Author  :   Aditya Divakaran 
@Version :   1.0
@Contact :   adi.develops@gmail.com 
@License :   MIT License, Aditya Divakaran
@Desc    :   Testing script
"""

import pytest
from lib.calculator.calculator import Calculator


class TestCalculator:
    """Class to test Calculator"""

    # Testing getters
    @pytest.mark.getter
    @pytest.mark.parametrize("num1, num2", [(1, 2), (2, 3), (-1, -1), (0, 0)])
    def test_num1(self, num1, num2):
        """Initialization of num1"""
        t_c = Calculator(num1, num2)
        assert t_c.num1 == num1

    @pytest.mark.getter
    @pytest.mark.parametrize("num1, num2", [(1, 2), (2, 3), (-1, -1), (0, 0)])
    def test_num2(self, num1, num2):
        """Initialization of num2"""
        t_c = Calculator(num1, num2)
        assert t_c.num2 == num2

    # Testing setters
    @pytest.mark.setter
    @pytest.mark.parametrize("num1, num2", [(1, 2), (2, 3), (-1, -1), (0, 0)])
    def test_set_num1(self, num1, num2):
        """Setter method of num1"""
        t_c = Calculator(num2=num2)
        t_c.num1 = num1
        assert t_c.num1 == num1

    @pytest.mark.setter
    @pytest.mark.parametrize("num1, num2", [(1, 2), (2, 3), (-1, -1), (0, 0)])
    def test_set_num2(self, num1, num2):
        """Setter method of num2"""
        t_c = Calculator(num1=num1)
        t_c.num2 = num2
        assert t_c.num2 == num2

    # Testing static methods
    @pytest.mark.static
    @pytest.mark.parametrize(
        "num1, num2, result", [(1, 2, 3), (2, 3, 5), (-1, -1, -2), (0, 0, 0)]
    )
    def test_static_add(self, num1, num2, result):
        """Static addition method"""
        assert Calculator._add(num1, num2) == result

    @pytest.mark.static
    @pytest.mark.parametrize(
        "num1, num2, result", [(1, 2, -1), (2, 3, -1), (-1, -1, 0), (0, 0, 0)]
    )
    def test_static_subtract(self, num1, num2, result):
        """Static subtraction method"""
        assert Calculator._subtract(num1, num2) == result

    @pytest.mark.static
    @pytest.mark.parametrize(
        "num1, num2, result", [(1, 2, 2), (2, 3, 6), (-1, -1, 1), (0, 0, 0)]
    )
    def test_static_multiply(self, num1, num2, result):
        """Static multiplication method"""
        assert Calculator._multiply(num1, num2) == result

    @pytest.mark.static
    @pytest.mark.parametrize(
        "num1, num2, result", [(1, 2, 0.5), (6, 3, 2), (-1, -1, 1)]
    )
    def test_static_divide(self, num1, num2, result):
        """Static division method"""
        assert Calculator._divide(num1, num2) == result

    @pytest.mark.static
    def test_static_divide0(self):
        """Static addition method for 0 denominator"""
        with pytest.raises(ZeroDivisionError):
            Calculator._divide(1, 0)

    # Testing class methods
    @pytest.mark.instance
    @pytest.mark.parametrize(
        "num1, num2, result", [(1, 2, 3), (2, 3, 5), (-1, -1, -2), (0, 0, 0)]
    )
    def test_add(self, num1, num2, result):
        """Class addition method"""
        t_c = Calculator(num1, num2)
        assert t_c.add() == result

    @pytest.mark.instance
    @pytest.mark.parametrize(
        "num1, num2, result", [(1, 2, -1), (2, 3, -1), (-1, -1, 0), (0, 0, 0)]
    )
    def test_subtract(self, num1, num2, result):
        """Class subtraction method"""
        t_c = Calculator(num1, num2)
        assert t_c.subtract() == result

    @pytest.mark.instance
    @pytest.mark.parametrize(
        "num1, num2, result", [(1, 2, 2), (2, 3, 6), (-1, -1, 1), (0, 0, 0)]
    )
    def test_multiply(self, num1, num2, result):
        """Class multiplication method"""
        t_c = Calculator(num1, num2)
        assert t_c.multiply() == result

    @pytest.mark.instance
    @pytest.mark.parametrize(
        "num1, num2, result", [(1, 2, 0.5), (6, 3, 2), (-1, -1, 1)]
    )
    def test_divide(self, num1, num2, result):
        """Class division method"""
        t_c = Calculator(num1, num2)
        assert t_c.divide() == result

    @pytest.mark.instance
    def test_divide0(self):
        """Class addition method with denominator 0"""
        with pytest.raises(ZeroDivisionError):
            t_c = Calculator(1, 0)
            t_c.divide()
