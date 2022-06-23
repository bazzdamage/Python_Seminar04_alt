# 2. Дан список чисел. Создать список в который попадают числа,
# описывающие возрастающую последовательность и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя
nums = [1, 5, 2, 3, 4, 6, 1, 7]
# nums = [5, 2, 3, 4, 6, 1, 7]


def longest_raising_sequence(seq):
    list_of_max = [0] * (len(seq))
    for i in range(0, len(seq)):
        max_in_seq = 0
        for j in range(0, i):
            if seq[i] > seq[j] and list_of_max[j] > max_in_seq:
                max_in_seq = list_of_max[j]
        list_of_max[i] = max_in_seq + 1
    max_index_of_seq = list_of_max.index(max(list_of_max))

    last_max = nums[max_index_of_seq]
    last_index_of_seq = max_index_of_seq
    lrs = []
    for i in range(max_index_of_seq, -1, -1):
        if last_index_of_seq - list_of_max[i] <= 1 and nums[i] <= last_max:
            lrs.insert(0, nums[i])
            last_index_of_seq = i - 1
            last_max = nums[i]

    return lrs


print(longest_raising_sequence(nums))

