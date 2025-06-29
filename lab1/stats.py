def mean(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mode(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    modes = [num for num, count in freq.items() if count == max_count]
    return min(modes)

if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = [float(x) for x in user_input.strip().split()]
        print(f"Mean: {mean(numbers)}")
        print(f"Median: {median(numbers)}")
        print(f"Mode: {mode(numbers)}")
    except ValueError as e:
        print(f"Error: {e}")