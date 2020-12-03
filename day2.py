input_file = open("./input2.txt", "r")
input_array = []
for line in input_file.readlines():
    sub_array = []
    elements = line.split(" ")
    char_range = elements[0].split("-")
    sub_array.append(int(char_range[0]))
    sub_array.append(int(char_range[1]))
    character = elements[1].strip(":")
    sub_array.append(character)
    password = elements[2].strip("\n")
    sub_array.append(password)
    input_array.append(sub_array)
good_pwd_count = 0
for policy in input_array:
    #min_num = policy[0]
    index1 = policy[0]
    #max_num = policy[1]
    index2 = policy[1]
    character = policy[2]
    password = policy[3]
    # Small optimization
    if character in password:
        # Part 2
        if (character == password[index1 - 1]) ^ (character == password[index2 - 1]):
            good_pwd_count += 1
        else:
            next
        
        # Part 1
        # num_occurences = password.count(character)
        # if num_occurences < min_num or num_occurences > max_num:
        #     next
        # else:
        #     good_pwd_count += 1
print(good_pwd_count)
