'''
MODES:
r -> read : open a file to read the data. if file is not available then
            will get FileNotFoundError
w -> write : Open a file to write. if the file is there it will remove the
            existing content of the file and start writing as a new file.
            if file is not there, it will create the file and write into it.
a -> append : Open a file to write. if the file is there it will not  remove the
            existing content rather it will continue to write as an additional lines.
            if file is not there, it will create the file and write into it.
r+->read and write : the must be there to read and after reading the exiting contnet then
                     we can start write the additional lines into it.
w+ -> write and read : write the data and read post write operation

rb -> read binary : used for reading the binary files (video's , audio. image)

wb-> write binary

READ:
    read(), readline(), readlines()
WRITE:
    write(), writelines()
'''
# Syntax:
# with open("filename","mode") as file_handler:
#     statement

# with open(r'D:\TPERSONAL\python_ericsson\days.txt','r') as fh:
#     #print(fh.read())
#     #print(fh.readline(),end='')
#     for x in fh.readlines()[1:6]:
#         print(x,end='')

# with open(r'D:\TPERSONAL\python_ericsson\tech.txt','w') as x:
#     #x.write("Python")
#     x.writelines(["Python\n","Machine Learning\n","AWS\n","Oracle"])

# with open(r'D:\TPERSONAL\python_ericsson\technology.txt','a') as x:
#     #x.write("Python")
#     x.writelines(["Python\n","Machine Learning\n","AWS\n","Oracle"])

# with open('tech.txt','r+') as f:
#     print(f.read())
#     f.write("\nAIML")

# with open('tech.txt','w+') as f:
#     f.writelines(["Chennai\n","Mumbai\n","Delhi\n","Bangalore"])
#     f.seek(0,0)
#     print(f.read())

# with open(r'C:\Users\RaghulRamesh\OneDrive\Pictures\puppy.jpg','rb') as fo:
#     with open(r'C:\Users\RaghulRamesh\OneDrive\Pictures\puppy_tuesday.jpg', 'wb') as wo:
#         wo.write(fo.read())