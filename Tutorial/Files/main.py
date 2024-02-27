# open a file in read mode
test_file = open('D:\\WS\\Python\\Tutorial\\Files\\test.txt')

# read the file content
test_content = test_file.read()
print(test_content)

"""
Mode	Description
r	Open a file in reading mode (default)
w	Open a file in writing mode
x	Open a file for exclusive creation 
a	Open a file in appending mode (adds content at the end of the file)
t	Open a file in text mode (default)
b	Open a file in binary mode
+	Open a file in both read and write mode

# open a file in default mode (read and text)
file1 = open("test.txt")      # equivalent to open("test.txt", "rt")

# open a file in write and text mode 
file1 = open("test.txt",'w')  

# open a file in read, write and binary mode
file1 = open("img.bmp",'+b') 
"""

# Writing to Files
test2_file_name = 'D:\\WS\\Python\\Tutorial\\Files\\test2.txt'
test2_file = open(test2_file_name, 'w')
test2_file.write('Programming is fun.\n')
test2_file.write('Python is fun.')

# close the file after reading
test_file.close()
test2_file.close()

# Opening a File Using with...open
with open(test2_file_name, "r") as test2_file:
    test_content = test2_file.read()
    print(test_content)
    test2_file.close()

# Exception Handling in Files
try:
    test2_file = open(test2_file_name, "r")
    read_content = test2_file.read()
    print(read_content)

finally:
    # close the file
    test2_file.close()