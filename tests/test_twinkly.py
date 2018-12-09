#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `twinkly` package."""

import pytest

from twinkly.twinkly import Twinkly

def test_device_exists():
	twinkly = Twinkly("192.168.30.29")
	assert twinkly.login_auth()
