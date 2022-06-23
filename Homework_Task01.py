# Создать и заполнить файл случайными целыми значениями.
# Выполнить сортировку содержимого файла по возрастанию.
import random


def generate_randint_file(filename: str, count: int):
    with open(filename, 'w') as f:
        for i in range(count):
            f.write(str(random.randint(1, 100)) + "\n")


def sorting_file(filename: str):
    with open(filename, 'r') as f:
        initial = f.read().splitlines()
        result = list(map(int, initial))
        result.sort()
        print(result)
    with open(filename, 'w') as f:
        for i in result:
            f.write(f'{i}\n')
    return result


generate_randint_file('task01_result', 10)
print(sorting_file('task01_result'))
