from gnr.app.gnrapp import GnrApp
import pytest


def setup_module(module):
    module.INSTANCE_NAME = 'sandboxpg'

class TestPivotTable:
    def setup_class(cls):
        cls.app = GnrApp(INSTANCE_NAME)
        cls.db = cls.app.db


    def test_simple_pivot(self):
        pass
