from dao.base_dao import BaseDao
from models.stock import Stock
import pytest


class TestBaseDao:
    @pytest.fixture
    def base_dao_model_instance(self):
        return BaseDao(Stock)

    def test_base_dao_instance(self, base_dao_model_instance):
        assert isinstance(base_dao_model_instance, BaseDao)
