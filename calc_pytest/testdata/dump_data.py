import yaml

test_data_add = [
    (1, 1, 2),
    (100, 200, 300),
    (-22, -30, -52),
    (10, -5, 5),
    (0.1, 0.2, 0.3)
]

test_data_sub = [
    (1, 1, 0),
    (100, 200, -100),
    (-22, -30, 8),
    (10, -5, 15),
    (0.1, 0.2, -0.1)
]

test_data_mul = [
    (1, 1, 1),
    (100, 200, 20000),
    (-22, -30, 660),
    (10, -5, -50),
    (0.1, 0.2, 0.02)
]

test_data_div = [
    (1, 1, 1),
    (100, 200, 0.5),
    (-22, -30, 0.73),
    (10, -5, -2),
    (0.1, 0.2, 0.5),
    (100, 0, 123)
]

with open("data_add.yml", "w") as f:
    yaml.safe_dump(test_data_add, f)

with open("data_sub.yml", "w") as f:
    yaml.safe_dump(test_data_sub, f)

with open("data_mul.yml", "w") as f:
    yaml.safe_dump(test_data_mul, f)

with open("data_div.yml", "w") as f:
    yaml.safe_dump(test_data_div, f)