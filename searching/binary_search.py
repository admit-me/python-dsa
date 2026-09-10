def binary_search(numbers, target):
    left, right = 0, len(numbers) - 1
    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == "__main__":
    values = [1, 3, 5, 7, 9, 11]
    print(binary_search(values, 7))
