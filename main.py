#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   main.py
@Time    :   2022/06/25 20:01:07
@Author  :   Aditya Divakaran
@Version :   1.0
@Contact :   adi.develops@gmail.com
@License :   MIT License, Aditya Divakaran
@Desc    :   Python-template testing project's main script
"""

from lib.calculator.calculator import Calculator

ca = Calculator(5, 6)
print("Object made")
# print(Calculator._add(1, 2)) # Not recommended but noted for testing purposes
print(ca.num1)
ca.num2 = 5
print(ca.add())
print("Object add called")
print("Done.")
