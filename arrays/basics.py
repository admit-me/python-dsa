def find_max(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum


def remove_duplicates(numbers):
    seen = set()
    result = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result


if __name__ == "__main__":
    data = [4, 2, 9, 2, 7, 4, 1]
    print("Maximum:", find_max(data))
    print("Unique values:", remove_duplicates(data))
