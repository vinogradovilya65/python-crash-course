# Use the code from previous task to write
# the body of the function that returns
# a list which contains integers in a range [1; n]
#
# If argument `reverse` is set to `True`, the function
# must return a list which contains integers in a range [n; 1]
def fill(n: int, reverse: bool = False) -> list[int]:
    if reverse:
        return list(range(n, 0, -1))  # От n до 1 включительно
    else:
        return list(range(1, n + 1))  # От 1 до n включительно


# Do not change the below's code
if __name__ == "__main__":
    assert fill(3) == [1, 2, 3]
    assert fill(0) == []
    assert fill(4) == [1, 2, 3, 4]
    assert fill(1) == [1]

    assert fill(3, True) == [3, 2, 1]
    assert fill(0, True) == []
    assert fill(4, True) == [4, 3, 2, 1]
    assert fill(1, True) == [1]
