import os

def main():

    set_files = set()
    set_directories = set()

    for root,directories,files in os.walk("/home/itaira/proj_py/py_general_projects/Scripting with Python and SQL for Data Engineering"):

        for file in files:
            absolute_path = os.path.join(root,file)
            #Collecting files
            set_files.add(absolute_path)
        
        for directory in directories:
            absolute_path = os.path.join(root,directory)
            #Collecting directories
            set_directories.add(absolute_path)

    print("-------------Files list")        
    for file in set_files:
        print(f"File path: {file}")
    
    print("-------------Directories list")
    for directory in set_directories:
        print(f"Directory path: {directory}")


if __name__ == "__main__":
    main()