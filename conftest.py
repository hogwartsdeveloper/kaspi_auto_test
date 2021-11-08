import pytest


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox',
                     help="Choose brower: chrome or firefox")