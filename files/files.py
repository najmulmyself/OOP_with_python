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


#IMPORTANT!
#read() and readlines() has a diffrence | read just like read the file content and readlines() return a list of content 
#for refs: https://www.w3schools.com/python/ref_file_readlines.asp


#WRITING A FILE
#WRITING A FILE NEDD TO SPECIFY THE MODE="W" | BY DEFAULT THE MODE IS MODE = "R";
#no need to mention mode = "" we can just pass the mode value;

with open("test.txt", "w") as file:
    content = file.write("New Text")
    print(content) 
    
    #if we use mode="w" it will replace the the existing text and write the new line
    #if we want to add more lines in our files need to change the mode to mode="a" this simply means append the text to the existing file

with open("test.txt", "a") as file:
    content = file.write("\nNew Text with new line")
    print(content) 


#if we set the file name which doesn't even exits in our directory , write mode will create a new file for us | this only works in write mode
