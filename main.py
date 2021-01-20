import random
import os
import shutil

'''
Creates a set number of randomly named files in the supplied directory
'''
def create_random_files(directory_path, num_files):

    #FOR i = 0; i < num_files; i++
    for i in range(num_files):

        #build full file path
        file_name = str(random.randint(0, 1000)) + ".txt"
        file_path = os.path.join(directory_path, file_name)

        #ensure that directory exists
        if os.path.exists(directory_path) == False:
            os.makedirs(directory_path)

        #save file
        with open(file_path, "w") as random_file:
            print(random.randint(0, 999), file=random_file)

'''
Deletes all files in a directory
https://linuxize.com/post/python-delete-files-and-directories/
'''
def clean_directory(directory_name):
    shutil.rmtree(directory_name)

    '''delete files individually
    for (dirpath, dirnames, filenames) in os.walk(directory_name):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            os.remove(file_path)
    '''
create_random_files('folder3', 100)
clean_directory('folder3')
print("done")
