import json

INPUT_FILE = 'input.json'


def task() -> float:
    sum_ = 0

    with open(INPUT_FILE, 'r') as f:
        file = json.load(f)
    for i in file:
        prod = i.get('score', 0) * i.get('weight', 0)
        sum_ += prod
    return round(sum_, 3)


print(task())
