# Swapping the value of two variables


def swap(var1, var2):
    # Simple and quick way
    var1, var2 = var2, var1

    # Old School implementation
    # temp = var1
    # var1 = var2
    # var2 = temp

    return var1, var2


print(swap("Test", "Result"))
