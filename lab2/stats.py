def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    nums = sorted(numbers)
    n = len(nums)
    mid = n // 2
    if n % 2 == 1:
        return nums[mid]
    else:
        return (nums[mid - 1] + nums[mid]) / 2

def mode(numbers):
    if not numbers:
        return 0
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    for num in freq:
        if freq[num] == max_count:
            return num

def main():
    test_list = [1, 2, 2, 3, 4]
    print("Test List:", test_list)
    print("Mean:", mean(test_list))
    print("Median:", median(test_list))
    print("Mode:", mode(test_list))

    print("\n--- User Input ---")
    user_input = input("Enter a list of numbers separated by spaces: ")
    user_list = list(map(int, user_input.split()))
    print("User List:", user_list)
    print("Mean:", mean(user_list))
    print("Median:", median(user_list))
    print("Mode:", mode(user_list))

if __name__ == "__main__":
    main()