import pytest
from src.lib.time import parse_time_string, format_time

def test_parse_time_string_valid():
    # 4 parts
    assert parse_time_string("00:01:26:123000") == 86.123
    assert parse_time_string("00:01:26.123000") == 86.123
    # 3 parts (micro)
    assert parse_time_string("01:26.123") == 86.123
    # 3 parts (no micro)
    assert parse_time_string("00:01:26") == 86.0
    # 2 parts
    assert parse_time_string("01:26") == 86.0
    # Timedelta format
    assert parse_time_string("0 days 00:01:27.060000") == 87.06

def test_parse_time_string_invalid():
    assert parse_time_string("") is None
    assert parse_time_string("   ") is None
    assert parse_time_string(None) is None
    assert parse_time_string("123") is None
    assert parse_time_string("1:2:3:4:5") is None
    assert parse_time_string("01:26.abc") is None
    assert parse_time_string("hh:mm:ss") is None

def test_format_time():
    assert format_time(86.123) == "01:26.123"
    assert format_time(0) == "00:00.000"
    assert format_time(-1) == "N/A"
    assert format_time(None) == "N/A"
