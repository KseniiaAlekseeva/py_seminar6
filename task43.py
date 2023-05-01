def count_couples(some_list: list) -> int:
    # count = 0
    # for i in set(some_list):
    #     num = some_list.count(i)
    #     if num > 1:
    #         count += num//2
    # return count
    return sum(some_list.count(i)//2 for i in set(some_list))


first = [1, 2, 1, 3, 4, 5, 3, 4]
second = [1, 2, 1, 3, 4, 3, 1]

print(count_couples(first))
print(count_couples(second))
