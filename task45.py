def sum_del(num: int) -> int:
    # count = 0
    # for i in range(1, num//2+1):
    #     if num % i == 0:
    #         count += i
    # return count
    return sum(i for i in range(1, num//2+1) if num % i == 0)


k = int(input("Enter a natural k: "))

# for i in range(1, k+1):
#     if i == sum_del(sum_del(i)) and i < sum_del(i):
#         print(i, sum_del(i))

result = [(i, sum_del(i)) for i in range(1, k+1) if i ==
          sum_del(sum_del(i)) and i < sum_del(i)]
print(result)
