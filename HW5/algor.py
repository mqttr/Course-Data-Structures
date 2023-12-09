import hashing
import sorting

def n_squared_algorithm(target_value: int, unsorted_list: list[int]) -> tuple[ int, int ]:
    for i, i_val in enumerate(unsorted_list):
        # Skips iteration if i_val is too large.
        if i_val >= target_value:
            continue

        for j, j_val in enumerate(unsorted_list[i:]):
            if i_val + j_val == target_value:
                # print(i, i_val, j, j_val)
                return (i_val, j_val)
            
    return None

def n_log_n_algorithm(target_value: int, unsorted_list: list[int]) -> tuple[ int, int ]:
    return None

def linear_n_algorithm(target_value: int, unsorted_list: list[int]) -> tuple[ int, int ]:
    table: hashing.HashTable = hashing.HashTable(len(unsorted_list)*2)

    for integer in unsorted_list:
        if integer < target_value:
            table.insert(integer)
    print("finish building")
    for value in range(1, target_value):
        if not table.contains(value):
            continue

        j_val = target_value-value
        if table.contains(j_val):
            return (value, j_val)


if __name__ == "__main__":
    import random
    cnt = 9999999
    sample = random.sample(range(1, cnt+1), cnt)

    if 2 in sample:
        print("2 in sample")
    if 1 in sample:
        print("1 in sample")


    import time
    print('start')
    start = time.perf_counter()
    i, j = n_squared_algorithm(3, sample)
    end = time.perf_counter()
    print('end')
    print(f'{end-start}')
    print(i, j)

    print('start')
    start = time.perf_counter()
    i, j = linear_n_algorithm(3, sample)
    end = time.perf_counter()
    print('end')
    print(f'{end-start}')

    print(i, j)