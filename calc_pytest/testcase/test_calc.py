import pytest
import sys
import os
sys.path.append(os.pardir)
import calc_pytest.src.calculator as calc
import yaml

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def get_data(key, filename=os.path.join(BASE_PATH, "../testdata/datas.yml")):
    with open(filename, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data.get(key)


class TestCalc(object):
    def setup_class(self):
        self.calc = calc.Calc()

    # @pytest.mark.parametrize("a, b, result", [
    #     (1, 1, 2),
    #     (1, 2, 3),
    #     (2, 2, 4),
    # ], ids=["test1", "test2", "test3"])
    @pytest.mark.parametrize("a, b , result",
                             get_data("test_data_add").values(),
                             ids=get_data("test_data_add").keys())
    @pytest.mark.add
    def test_add(self, a, b, result):
        assert result == round(self.calc.add(a, b), 2)

    @pytest.mark.parametrize("a, b, result",
                             get_data("test_data_sub").values(),
                             ids=get_data("test_data_sub").keys())
    @pytest.mark.sub
    def test_sub(self, a, b, result):
        assert result == round(self.calc.sub(a, b), 2)

    @pytest.mark.parametrize("a, b, result",
                             get_data("test_data_mul").values(),
                             ids=get_data("test_data_mul").keys())
    @pytest.mark.mul
    def test_mul(self, a, b, result):
        assert result == round(self.calc.mul(a, b), 2)

    @pytest.mark.parametrize("a, b, result",
                             get_data("test_data_div").values(),
                             ids=get_data("test_data_div").keys())
    @pytest.mark.div
    def test_div(self, a, b, result):
        if b == 0:
            raise ZeroDivisionError
        assert result == round(self.calc.div(a, b), 2)


if __name__ == '__main__':
    pytest.main()
