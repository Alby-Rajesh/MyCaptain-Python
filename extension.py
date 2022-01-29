import os
file_name = input("Enter the filename with extension:")
b=os.path.splitext(file_name)
print("The extension is:",b[1])
