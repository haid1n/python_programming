# Imported library
import os


# Get the current working directory
cwd = os.getcwd()

print("Current working directory :", cwd)


# Change the current working directory
os.chdir("../")

print(os.getcwd())


# Used to delete a file path
# Cannot delete a directory
file = "New Text Document (2).txt"

location = "C:/Users/chari plus/Documents"

path = os.path.join(location, file)
 
#os.remove(path)


# Create a new directory
# Raise error if it already exist
directory = "Geeks"

parent_dir = "C:/Users/chari plus/Documents/"

# Provide read and write permissions 
# Without it the directory will have no mode
mode = 0o666

path_1 = os.path.join(parent_dir, directory)

#os.mkdir(path_1, mode)

print("Directory '% s' created" % directory)


# Delete an empty directory
# os.rmdir(path_1)


# List files and directories
path = "C:/Users/chari plus/Documents/Tokyo Revengers"

dir_list = os.listdir(path)

print("Files and directories in ", path, " :") 

print(dir_list) 


 