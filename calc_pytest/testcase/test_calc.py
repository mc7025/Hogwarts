import pytest
import sys
import os
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.pardir)

import calc_pytest.src.calculator as calc
import yaml


def get_data():
    with open(os.path.join(BASE_PATH, "../testdata/datas.yml"), encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


class TestCalc(object):
    def setup_class(self):
        self.calc = calc.Calc()

    # @pytest.mark.parametrize("a, b, result", [
    #     (1, 1, 2),
    #     (1, 2, 3),
    #     (2, 2, 4),
    # ], ids=["test1", "test2", "test3"])
    @pytest.mark.parametrize("a, b , result",
                             get_data().get("test_data_add"))
    @pytest.mark.add
    def test_add(self, a, b, result):
        assert result == round(self.calc.add(a, b), 2)

    @pytest.mark.parametrize("a, b, result",
                             get_data().get("test_data_sub"))
    @pytest.mark.sub
    def test_sub(self, a, b, result):
        assert result == round(self.calc.sub(a, b), 2)

    @pytest.mark.parametrize("a, b, result",
                             get_data().get("test_data_mul"))
    @pytest.mark.mul
    def test_mul(self, a, b, result):
        assert result == round(self.calc.mul(a, b), 2)

    @pytest.mark.parametrize("a, b, result",
                             get_data().get("test_data_div"))
    @pytest.mark.div
    def test_div(self, a, b, result):
        if b == 0:
            raise ZeroDivisionError
        assert result == round(self.calc.div(a, b), 2)


if __name__ == '__main__':
    pytest.main()
