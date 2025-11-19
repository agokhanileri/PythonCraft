a = 2
print(a * 2)

my_str = "abc"
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.update({7, 8})
print(my_set)

## ----------
nums = [1, 2, 3, 4]
for num in filter(lambda x: (x % 2) == 0, nums):
    print("found even: " + str(num))
