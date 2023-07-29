from time import time
nums, target = [2, 7, 11, 15, 4, 9, 4, 7, 3, 4, 5, 6, 1, 9, 7, 11, 88, 999, 23, 123, 5, 3, 2, 6, 7, 12, 1, 4, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 13

s1 = time()
# O(N)
for i in range(len(nums)):
     for j in range(i+1, len(nums)):
         if nums[i] + nums[j] == 9: 
             print(f'{nums[i]} + {nums[j]} = {target}')
e1 = time()
# O(N)
num_set = set()
for num in nums: 
    complement = target - num
    if complement in num_set:
        print(complement, num)
    num_set.add(num)
e2=time()

print(f'I: {e2-s1}s, II: {e2-e1}s')