import random
import os
import shutil
import pathlib
import datetime

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

'''
Merges source_folder files into sink_folder
'''
def merge_files(source_folder, sink_folder):
    merge_counter = 0
    merged_files = []
    for (dirpath, dirnames, filenames) in os.walk(source_folder):
        for file in filenames:
            source_file_path = os.path.join(dirpath, file)
            sink_file_path = os.path.join(sink_folder, file)
            
            #what if the file alraedy exists in sink folder?
            should_write = True
            if os.path.exists(sink_file_path) == True:
                source_file_info = pathlib.Path(source_file_path)
                sink_file_info = pathlib.Path(sink_file_path)

                source_last_modified = datetime.datetime.fromtimestamp(source_file_info.stat().st_mtime)
                sink_last_modified = datetime.datetime.fromtimestamp(sink_file_info.stat().st_mtime)
                #print("file name:", file, "source time:", source_last_modified, "sink time:", sink_last_modified)
                if source_last_modified < sink_last_modified:

                    #newer file in sink, so don't overwrite sink version
                    should_write = False
            
            if should_write == True:
                shutil.move(source_file_path, sink_file_path)
                merge_counter += 1
                merged_files.append(file)
    return (merge_counter, merged_files)


clean_directory('folder1')
clean_directory('folder2')
create_random_files('folder1', 100)
create_random_files('folder2', 100)
result = merge_files('folder1', 'folder2')
print("done.  Merged", result[0] , "files.")
print(result[1])