import pytest
from pythoncode.caculator import Calculator
import yaml


def get_datas():
    with open("./data1.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["adddata"]
        div_datas = datas["divdata"]
        sub_datas = datas["subdata"]
        mul_datas = datas["muldata"]
        return [add_datas, div_datas, sub_datas, mul_datas]


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    @pytest.mark.parametrize("a, b, expect", get_datas()[0])
    @pytest.mark.run(order=1)
    def test_add(self, a, b, expect, print_message):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", get_datas()[1])
    @pytest.mark.run(order=4)
    def test_div(self, a, b, expect, print_message):
        result = self.calc.div(a, b)
        assert result == expect

    @pytest.mark.parametrize("a , b, expect", get_datas()[2])
    @pytest.mark.run(order=2)
    def test_sub(self, a, b, expect, print_message):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize("a ,b , expect", get_datas()[3])
    @pytest.mark.run(order=3)
    def test_mul(self, a, b, expect, print_message):
        result = self.calc.mul(a, b)
        assert result == expect
