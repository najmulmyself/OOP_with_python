# READING A FILE

file = open("test.txt")
# i want to read the file with read() func and save it to a variable
read_file = file.read()

print(read_file)

#this is the basic method of opening a file and file need to close manually by commanding close()

file.close()

#theres another way to open a file without closing the file | it will automatically do this for me

with open("test.txt") as file:
    content = file.read()
    print(content) 
    # no need to close the file