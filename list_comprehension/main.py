with open("file_1.txt") as file:
    file1 = file.read()
    list = [file for file in file1.split()]

for n in list:
    con = int(n)
    if(con % 2 == 0):
        print(con)
