input_file = open("./input1.txt", "r")
nums = []
for line in input_file.readlines():
    line_to_int = int(line)
    nums.append(line_to_int)
correct_num1 = None
correct_num2 = None
correct_num3 = None
for index1 in range(0, len(nums)- 1):
    # This is a set of combinations so order doesn't matter
    # ergo the shortcut
    for index2 in range(index1 + 1, len(nums)-1):
        for index3 in range(index2 + 1, len(nums)-1):
            num1 = nums[index1]
            num2 = nums[index2]
            num3 = nums[index3]
            num_sum = num1 + num2 + num3
            if num_sum == 2020:
                correct_num1 = num1
                correct_num2 = num2
                correct_num3 = num3
                break
        if correct_num1:
            break
    if correct_num1:
        break
result = correct_num1 * correct_num2 * correct_num3
print(correct_num1)
print(correct_num2)
print(correct_num3)
print(result)