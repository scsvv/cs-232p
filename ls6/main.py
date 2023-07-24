from random import randint

nums = list()

for i in range(15):
    nums.append(randint(-100, 100))

ma, mi = nums[0], nums[0]

for num in nums:
    if num > ma: 
        ma = num
        continue
    if num < mi: 
        mi = num

print(nums, '\n\n')

print(f'1: {mi}, {ma}')
print(f'2: {min(nums)}, {max(nums)}')

nums.sort()
print(f'3: {nums[0]}, {nums[len(nums)-1]}')