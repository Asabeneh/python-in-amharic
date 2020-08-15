# We will continue tuple, and dictionary next week
tpl = tuple()
print(tpl)
nums = (1, 2, 3, 4, 1, 5)
print(nums)
print(len(nums))
print(nums.count(1))
print(nums.index(4))
lastIndex = len(nums)-1
print(nums[lastIndex])
print(nums[-3:-1])

set_of_nums = set(nums)
print(set_of_nums)
list_of_nums = list(nums)
print(list_of_nums)

tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
tpl3 = tpl1 + tpl2
print(tpl3)

for num in tpl3:
    print(num * num)
del tpl1

print(tpl2)
# print(tpl1)
