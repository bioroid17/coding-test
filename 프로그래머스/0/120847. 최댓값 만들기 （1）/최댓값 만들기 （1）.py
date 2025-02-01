def solution(numbers):
    sort_nums = sorted(numbers)
    return sort_nums[-1] * sort_nums[-2]