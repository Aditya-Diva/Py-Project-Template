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
# Load startup (Settings/config loaded before actual program runs)
import logging
from lib.utils import startup
from lib.calculator.calculator import Calculator

# Initialize startup actions
startup.__init__()
# Load logging of script
log = logging.getLogger(__name__)

ca: Calculator = Calculator(5, 6)
print("We made a calc object above!")

log.info("Object made")
# print(Calculator._add(1, 2)) # Not recommended but noted for testing purposes

log.debug(ca.num1)
log.debug(ca.num2)

ca.num2 = 5
log.info(ca.add())
log.info("Object add called")

log.warning("Test warning message.")
log.error("Test error message.")
log.critical("Test critical message.")

log.info("Done.")
