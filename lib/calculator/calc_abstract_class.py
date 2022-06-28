#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   CalcAbstractClass.py
@Time    :   2022/06/27 19:06:33
@Author  :   Aditya Divakaran
@Version :   1.0
@Contact :   adi.develops@gmail.com
@License :   MIT License, Aditya Divakaran
@Desc    :   Abstract class
"""

from abc import (
    ABC,
    abstractmethod,
    abstractproperty,
    abstractstaticmethod,
)


class CalcAbstractClass(ABC):
    """Abstract class for Calculator class
    Meant to act as a blueprint

    Args:
        ABC (_type_): importing ABC as parent for abstract class implementation
    """

    @abstractmethod
    def __init__(self) -> None:
        pass

    # Getter properties
    @abstractproperty
    def num1(self):
        """Num1 getter method"""

    @abstractproperty
    def num2(self):
        """Num2 getter method"""

    # Static methods
    @abstractstaticmethod
    def _add(num1: int, num2: int) -> int:
        """Static method for addition"""

    @abstractstaticmethod
    def _subtract(num1: int, num2: int) -> int:
        """Static method for subtraction"""

    @abstractstaticmethod
    def _multiply(num1: int, num2: int) -> int:
        """Static method for multiplication"""

    @abstractstaticmethod
    def _divide(num1: int, num2: int) -> int:
        """Static method for division"""

    # Class methods
    @abstractmethod
    def add(self):
        """Class method for addition"""

    @abstractmethod
    def subtract(self):
        """Class method for subtraction"""

    @abstractmethod
    def multiply(self):
        """Class method for multiplication"""

    @abstractmethod
    def divide(self):
        """Class method for division"""
