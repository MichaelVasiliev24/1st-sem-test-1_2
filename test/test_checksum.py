import pytest

from src.checksum import modulo_11_checksum


def test_good():
    assert modulo_11_checksum("2-266-11156-8")


def test_bad():
    assert not modulo_11_checksum("2-266-11156-3")


def test_less_chars():
    with pytest.raises(
        Exception,
        match="Количество значащих символов, то есть не считая пробелов и тире, в ISBN номере должно равняться 10.",
    ):
        modulo_11_checksum("2 35")


def test_more_chars():
    with pytest.raises(
        Exception,
        match="Количество значащих символов, то есть не считая пробелов и тире, в ISBN номере должно равняться 10.",
    ):
        modulo_11_checksum("123456789011")


def test_inappropriate_chars():
    with pytest.raises(
        Exception,
        match="ISBN может содержать только арабские цифры, а также римскую цифру X для контрольной цифры.",
    ):
        modulo_11_checksum("dfgdfg")
