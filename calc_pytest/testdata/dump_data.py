import yaml

test_datas = {
    "test_data_add": {
        "add_case1": (1, 1, 2),
        "add_case2": (100, 200, 300),
        "add_case3": (-22, -30, -52),
        "add_case4": (10, -5, 5),
        "add_case5": (0.1, 0.2, 0.3),
    },
    "test_data_sub": {
        "sub_case1": (1, 1, 0),
        "sub_case2": (100, 200, -100),
        "sub_case3": (-22, -30, 8),
        "sub_case4": (10, -5, 15),
        "sub_case5": (0.1, 0.2, -0.1),
    },
    "test_data_mul": {
        "mul_case1": (1, 1, 1),
        "mul_case2": (100, 200, 20000),
        "mul_case3": (-22, -30, 660),
        "mul_case4": (10, -5, -50),
        "mul_case5": (0.1, 0.2, 0.02)
    },
    "test_data_div": {
        "div_case1": (1, 1, 1),
        "div_case2": (100, 200, 0.5),
        "div_case3": (-22, -30, 0.73),
        "div_case4": (10, -5, -2),
        "div_case5": (0.1, 0.2, 0.5),
        "div_case6": (100, 0, 123)
    },
}
# with open("data_add.yml", "w") as f:
#     yaml.safe_dump(test_datas.get("test_data_add"), f)
#
# with open("data_sub.yml", "w") as f:
#     yaml.safe_dump(test_datas.get("test_data_sub"), f)
#
# with open("data_mul.yml", "w") as f:
#     yaml.safe_dump(test_datas.get("test_data_mul"), f)
#
# with open("data_div.yml", "w") as f:
#     yaml.safe_dump(test_datas.get("test_data_div"), f)

# with open("datas.yml", "w") as f:
#     yaml.safe_dump(test_datas, f)

with open("datas.yml") as f:
    data = yaml.safe_load(f)
    print(data)