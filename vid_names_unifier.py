import os, re

full_file_dir_path = os.path.join(os.path.dirname(__file__), "vids")
relative_path_with_system_separator = os.path.relpath(full_file_dir_path) + os.path.sep
onlyfiles = [f for f in os.listdir(full_file_dir_path) if os.path.isfile(os.path.join(full_file_dir_path, f))]

default_timestamp_lenght = 14
pattern = re.compile(r"(\D)*")
for file_name in onlyfiles:
    extension_index = str.rfind(file_name, ".")
    extension = file_name[extension_index:len(file_name)]
    no_extension_file_name = file_name[0:extension_index]
    original_timestamp = re.sub(pattern, "", no_extension_file_name)
    
    timestamp_lenght = len(original_timestamp)
    final_timestamp = original_timestamp
    if timestamp_lenght < default_timestamp_lenght:
        while timestamp_lenght < default_timestamp_lenght:
            print("Original timestamp: " + final_timestamp + " Next timestamp: " + final_timestamp + "0")
            final_timestamp = final_timestamp + "0"
            timestamp_lenght = len(final_timestamp)
        
    print(final_timestamp + " -> " + final_timestamp[0:default_timestamp_lenght])
    final_timestamp = final_timestamp[0:default_timestamp_lenght]
    final_file_name = "VID_" + final_timestamp + extension
    print(file_name + " -> " + final_file_name)
    try:
        os.rename(relative_path_with_system_separator + file_name, relative_path_with_system_separator + final_file_name)
    except FileExistsError as exception:
        print(final_file_name + " already exists. Deleting this file.")
        os.remove(relative_path_with_system_separator + file_name)