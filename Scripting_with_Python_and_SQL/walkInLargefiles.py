import os

# Persist the data into a dictionary. Since file paths are unique you can use those as dictionary keys
files = {}
for root, directories, _files in os.walk('.'):
    for _file in _files:
        full_path = os.path.join(root, _file)
        size = os.path.getsize(full_path)
        files[full_path] = size

print(type(files))