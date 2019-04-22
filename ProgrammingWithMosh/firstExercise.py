# # Control Flow Exercise
# evenCounter = 0
# for i in range(1, 10):
#     if (i % 2 == 0):
#         print(i)
#         evenCounter = evenCounter+1
# print(f"We have {evenCounter} even numbers")


def func(x):
    return x % 7


L = [15, 3, 11, 7]

print(f"Normal sort : {sorted(L)}")
print(f"Sorted with key: {sorted(L, key=func)}")
