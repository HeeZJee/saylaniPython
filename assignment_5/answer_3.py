"""
Answer # 3
    Write a Python function to print the even numbers from a given list.
"""


def evenIndex(nums):
    li = []
    for num in range(0,len(nums)):
        if nums[num] % 2 == 0:
            li.append(nums[num])
    return li
    
print(evenIndex([114,26,33,5,63,7,445,6,74,64,45.5,102.2,44]))