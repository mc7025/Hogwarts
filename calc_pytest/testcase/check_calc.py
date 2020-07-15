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


def test_env(cmdoption):
    env, datas = cmdoption
    print(f"当前使用环境是：{env}")
    data = datas.get("test_data_add").values()
    ids = datas.get("test_data_add").keys()
    print(data, ids)


class CheckCalc(object):
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
    # @pytest.mark.add
    # @pytest.mark.run(order=1)     ## 添加到hook中
    # @pytest.mark.dependency()
    def check_add(self, a, b, result):
        assert result == round(self.calc.add(a, b), 2)

    @pytest.mark.parametrize("a, b, result",
                             get_data("test_data_sub").values(),
                             ids=get_data("test_data_sub").keys())
    # @pytest.mark.sub
    # @pytest.mark.run(order=2)     ## 添加到hook中
    # @pytest.mark.dependency(depend=["check_add"])
    def check_sub(self, a, b, result):
        assert result == round(self.calc.sub(a, b), 2)

    @pytest.mark.parametrize("a, b, result",
                             get_data("test_data_mul").values(),
                             ids=get_data("test_data_mul").keys())
    # @pytest.mark.mul
    # @pytest.mark.run(order=3)     ## 添加到hook中
    # @pytest.mark.dependency()
    def check_mul(self, a, b, result):
        assert result == round(self.calc.mul(a, b), 2)

    @pytest.mark.parametrize("a, b, result",
                             get_data("test_data_div").values(),
                             ids=get_data("test_data_div").keys())
    # @pytest.mark.div
    # @pytest.mark.run(order=4)         ## 添加到hook中
    # @pytest.mark.dependency(depends=["check_mul"])
    def check_div(self, a, b, result):
        try:
            assert result == round(self.calc.div(a, b), 2)
        except ZeroDivisionError as e:
            print(f"除数为0，错误代码：{e}")


if __name__ == '__main__':
    pytest.main()
