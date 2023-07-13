import os,sys

current_directory = os.getcwd()+'/king'
k=0;
for filename in os.listdir(current_directory):
    if filename.endswith(".png"):
        # Construct the full path of the file
        current_path = os.path.join(current_directory, filename)

        # Construct the new filename
        new_filename = "{0}.png".format(k)
        k+=2
        # Construct the full path of the new file
        new_path = os.path.join(current_directory, new_filename)

        # Rename the file
        os.rename(current_path, new_path)

