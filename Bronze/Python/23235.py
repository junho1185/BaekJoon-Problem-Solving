n = 1
nums = [int(num) for num in input().split()]
while len(nums) > 1 or nums[0] != 0:
    print(f"Case {n}: Sorting... done!")
    n += 1
    nums = [int(num) for num in input().split()]