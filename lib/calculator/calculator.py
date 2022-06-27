#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   Calculator.py
@Time    :   2022/06/27 19:13:26
@Author  :   Aditya Divakaran
@Version :   1.0
@Contact :   adi.develops@gmail.com
@License :   MIT License, Aditya Divakaran
@Desc    :   Calculator Class
"""

from .calc_abstract_class import CalcAbstractClass


class Calculator(CalcAbstractClass):
    """Calculator Class reponsible for addition, subtraction,
    multiplication and division operations.

    Args:
        CalcAbstractClass (_type_): Abstract class inherited
                                    Enforces blueprint.
    """

    def __init__(self, num1: int = 1, num2: int = 1) -> None:
        """Initialization

        Args:
            num1 (int, optional): The first number. Defaults to 1.
            num2 (int, optional): The second number. Defaults to 1.
        """
        super().__init__()
        self._num1 = num1  # This is the first number
        self._num2 = num2  # This is the second number
        print(f"Calculator class instance initialized with numbers: {num1} {num2}")

    # Custom dunder/magic methods
    def __str__(self) -> str:
        """String dunder/magic method

        Returns:
            str: str for the instance
        """
        return (
            f"This is the str representation for calculator.\n"
            f"With nums loaded num1:{self._num1} num2:{self._num2}"
        )

    def __repr__(self) -> str:
        """Repr dunder/magic method

        Returns:
            str: raw repr for the instance
        """
        return (
            f"This is the raw representation for calculator.\n"
            f"With nums loaded num1:{self._num1} num2:{self._num2}"
        )

    def __len__(self) -> int:
        """Len dunder/magic method

        Returns:
            int: Returns expected length of class, with only num1 and num2,
                forcibly returning the value of 2, in this case
        """
        return 2

    # Getter functions
    @property
    def num1(self) -> int:
        """Getter function for protected variable num1

        Returns:
            int: Instance protected variable num1 value
        """
        return self._num1

    @property
    def num2(self) -> int:
        """Getter function for protected variable num2

        Returns:
            int: Instance protected variable num2 value
        """
        return self._num2

    # Setter functions
    @num1.setter
    def num1(self, value: int):
        """Setter function for protected variable num1

        Args:
            value (int): Value to assign to num1
        """
        self._num1 = value

    @num2.setter
    def num2(self, value: int):
        """Setter function for protected variable num2

        Args:
            value (int): Value to assign to num2
        """
        self._num2 = value

    # Static methods for actual operation
    @staticmethod
    def _add(num1: int = 0, num2: int = 0) -> int:
        """Addition operation on args

        Args:
            num1 (int, optional): First number. Defaults to 0.
            num2 (int, optional): Second number. Defaults to 0.

        Returns:
            int: Sum of args
        """
        return num1 + num2

    @staticmethod
    def _subtract(num1: int = 0, num2: int = 0) -> int:
        """Subtraction operation on args

        Args:
            num1 (int, optional): First number. Defaults to 0.
            num2 (int, optional): Second number. Defaults to 0.

        Returns:
            int: Difference of args
        """
        return num1 - num2

    @staticmethod
    def _multiply(num1: int, num2: int) -> int:
        """Multiplication operation on args

        Args:
            num1 (int, optional): First number.
            num2 (int, optional): Second number.

        Returns:
            int: Product of args
        """
        return num1 * num2

    @staticmethod
    def _divide(num1: int = 0, num2: int = 1) -> int:
        """Division operation on args.

        Args:
            num1 (int, optional): First number. Defaults to 0.
            num2 (int, optional): Second number. Defaults to 1.

        Raises:
            ZeroDivisionError: Explicitly raising it for testing
            purpose. As such already inbuilt in python.

        Returns:
            int: Quotient from division of args
        """
        # Division by zero check
        if num2 == 0:
            raise ZeroDivisionError(
                "Dev triggered message - Division by zero attempted. Not allowed."
            )
        return num1 / num2

    # Class methods which uses static methods (To avoid repetition and for testing)
    def add(self) -> int:
        """Addition property method

        Returns:
            int: Sum of member variables (num1, num2)
        """
        return Calculator._add(self._num1, self._num2)

    def subtract(self) -> int:
        """Subtraction property method

        Returns:
            int: Difference of member variables (num1, num2)
        """
        return Calculator._subtract(self._num1, self._num2)

    def multiply(self) -> int:
        """Multiplcation property method

        Returns:
            int: Product of member variables (num1, num2)
        """
        return Calculator._multiply(self._num1, self._num2)

    def divide(self) -> int:
        """Division property method

        Returns:
            int: Quotient of member variables (num1, num2)
        """
        return Calculator._divide(self._num1, self._num2)


if __name__ == "__main__":
    C = Calculator()
    print("Done.")
