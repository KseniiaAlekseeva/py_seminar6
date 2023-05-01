def count_neighbours(some_list: list) -> int:
    count = 0
    for i in range(len(some_list)):
        prev = some_list[i-1] if i > 0 else some_list[i]
        next = some_list[i+1] if i < len(some_list)-1 else some_list[i]
        if some_list[i] > prev and some_list[i] > next:
            count += 1
    return count


first = [5, 1, 3, 7, 9, 6]
second = [3, 4, 3, 6, 5, 8, 7]
print(count_neighbours(first))
print(count_neighbours(second))
