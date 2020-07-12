import pytest
import calc_pytest.src.calculator as calc


@pytest.fixture(autouse=True)
def s_t_fun(request):
    print("计算开始")
    yield
    print("计算结束")

