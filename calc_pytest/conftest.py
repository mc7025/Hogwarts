import sys
from typing import List

import pytest
import yaml
import os

BASEPATH = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(autouse=True)
def s_t_fun():
    print("计算开始")
    yield
    print("计算结束")


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
            item.add_marker(pytest.mark.run(order=1))
            item.add_marker(pytest.mark.dependency())
        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
            item.add_marker(pytest.mark.run(order=2))
            item.add_marker(pytest.mark.dependency(depend=["check_add"]))
        elif 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)
            item.add_marker(pytest.mark.run(order=3))
            item.add_marker(pytest.mark.dependency())
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
            item.add_marker(pytest.mark.run(order=4))
            item.add_marker(pytest.mark.dependency(depend=["check_mul"]))


def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env",
                      default="test",
                      dest='env',
                      help="set your run env")


@pytest.fixture(scope="session")
def cmdoption(request):
    myenv = request.config.getoption("--env", default="test")
    if myenv == "test":
        data_file = os.path.join(BASEPATH, "testdata/datas_test.yml")
    elif myenv == "dev":
        data_file = os.path.join(BASEPATH, "testdata/datas_dev.yml")
    elif myenv == "st":
        data_file = os.path.join(BASEPATH, "testdata/datas_st.yml")
    else:
        print("Error env. Using the default env.")
        data_file = os.path.join(BASEPATH, "testdata/datas_test.yml")

    with open(data_file, encoding='utf-8') as f:
        data = yaml.safe_load(f)

    return myenv, data


def pytest_generate_tests(metafunc: "Metafunc") -> None:
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.data,
                             ids=metafunc.mudule.ids,
                             scope="function")
