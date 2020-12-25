import pytest
from pythoncode.caculator import Calculator
import yaml


def get_datas():
    with open("./data1.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["adddata"]
        div_datas = datas["divdata"]
        return [add_datas, div_datas]


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def setup_method(self):
        print("\n开始计算")

    def teardown_method(self):
        print("\n结束计算")

    @pytest.mark.parametrize("a, b, expect", get_datas()[0])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", get_datas()[1])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect
