"""Module 9: คำนวณค่าทางสถิติเบื้องต้น"""

def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

def variance(numbers):
    m = mean(numbers)
    return sum((x - m) ** 2 for x in numbers) / len(numbers) if numbers else 0

def std_deviation(numbers):
    return variance(numbers) ** 0.5
