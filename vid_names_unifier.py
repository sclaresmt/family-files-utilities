import os, re

full_file_dir_path = os.path.join(os.path.dirname(__file__), "vids")
relative_path_with_system_separator = os.path.relpath(full_file_dir_path) + os.path.sep
onlyfiles = [f for f in os.listdir(full_file_dir_path) if os.path.isfile(os.path.join(full_file_dir_path, f))]

pattern = re.compile(r"(\D)*")
for file_name in onlyfiles:
    extension_index = str.rfind(file_name, ".")
    extension = file_name[extension_index:len(file_name)]
    no_extension_file_name = file_name[0:extension_index]
    final_file_name = "VID_" + re.sub(pattern, "", no_extension_file_name) + extension
    print(file_name + " -> " + final_file_name)
    os.rename(relative_path_with_system_separator + file_name, relative_path_with_system_separator + final_file_name)

    