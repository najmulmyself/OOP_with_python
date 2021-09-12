with open("file_1.txt") as file_1:
    file1 = file_1.readlines()


with open("file_2.txt") as file_2:
    file2 = file_2.readlines()


# format = [new_item for item in list if test]

result = [int(num) for num in file1 if num in file2]
print (result)