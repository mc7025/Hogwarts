import pytest
import calc_pytest.src.calculator as calc
import yaml


class TestCalc(object):
    def setup_class(self):
        self.calc = calc.Calc()

    # @pytest.mark.parametrize("a, b, result", [
    #     (1, 1, 2),
    #     (1, 2, 3),
    #     (2, 2, 4),
    # ], ids=["test1", "test2", "test3"])
    @pytest.mark.parametrize("a, b , result",
                             yaml.safe_load(
                                 open("../testdata/data_add.yml", encoding='utf-8')
                             ))
    @pytest.mark.add
    def test_add(self, a, b, result):
        assert result == round(self.calc.add(a, b), 2)

    @pytest.mark.parametrize("a, b, result",
                             yaml.safe_load(
                                 open("../testdata/data_sub.yml", encoding='utf-8')
                             ))
    @pytest.mark.sub
    def test_sub(self, a, b, result):
        assert result == round(self.calc.sub(a, b), 2)

    @pytest.mark.parametrize("a, b, result",
                             yaml.safe_load(
                                 open("../testdata/data_mul.yml", encoding='utf-8')
                             ))
    @pytest.mark.mul
    def test_mul(self, a, b, result):
        assert result == round(self.calc.mul(a, b), 2)

    @pytest.mark.parametrize("a, b, result",
                             yaml.safe_load(
                                 open("../testdata/data_div.yml", encoding='utf-8')
                             ))
    @pytest.mark.div
    def test_div(self, a, b, result):
        if b == 0:
            raise ZeroDivisionError
        assert result == round(self.calc.div(a, b), 2)


if __name__ == '__main__':
    pytest.main()