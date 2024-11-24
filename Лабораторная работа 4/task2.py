import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    list_ = []

    with open(INPUT_FILENAME, 'r') as f:

        column = f.readline().strip().split(',')

        for line_ in f:
            value = line_.strip().split(',')
            if len(value) == len(column):
                rows_dict = {column[i]: value[i] for i in range(len(column))}
                list_.append(rows_dict)

    new_string = json.dumps(list_, indent=4)

    with open(OUTPUT_FILENAME, 'w') as output_f:
        output_f.write(new_string)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
