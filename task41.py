def count_neighbours(some_list: list) -> int:
    count = 0
    for i in range(1, len(some_list)-1):
        if some_list[i] > some_list[i-1] and some_list[i] > some_list[i+1]:
            count += 1
    return count


first = [5, 1, 3, 7, 9, 6]
second = [3, 4, 3, 6, 5, 8, 7]
print(count_neighbours(first))
print(count_neighbours(second))
