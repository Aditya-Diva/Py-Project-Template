#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_startup.py
@Time    :   2022/08/19 12:05:02
@Author  :   Aditya Divakaran
@Version :   1.0
@Contact :   adi.develops@gmail.com
@License :   MIT License, Aditya Divakaran
@Desc    :   Test startup.py in utils
"""

import pytest
import os
import lib.utils.startup as startup


class TestStartup:
    """Class to test Startup"""

    @pytest.mark.main
    def test_init_debug_false(self):
        """Test __init__ function with debug_mode as false"""
        os.environ["DEBUG_MODE"] = "0"
        startup.__init__()

    @pytest.mark.main
    def test_init_debug_true(self):
        """Test __init__ function with debug_mode as true"""
        os.environ["DEBUG_MODE"] = "1"
        startup.__init__()

    @pytest.mark.main
    def test_init_valerr(self):
        """Test __init__ function with invalid value"""
        os.environ["DEBUG_MODE"] = "hey"
        with pytest.raises(SystemExit):
            startup.__init__()

    @pytest.mark.main
    def test_init_keyerr(self):
        """Test __init__ function with invalid key"""
        del os.environ["DEBUG_MODE"]
        with pytest.raises(SystemExit):
            startup.__init__()
