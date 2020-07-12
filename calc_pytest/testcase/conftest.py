import pytest


@pytest.fixture(autouse=True)
def s_t_fun():
    print("计算开始")
    yield
    print("计算结束")

