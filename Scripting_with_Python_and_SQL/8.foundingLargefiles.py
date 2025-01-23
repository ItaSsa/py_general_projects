import os

def traversing(dir):
    # Persist the data into a dictionary. Since file paths are unique you can use those as dictionary keys
    file_metadata = {}
    for root, directories, files in os.walk(dir):
        for _file in files:
            full_path = os.path.join(root, _file)
            size = os.path.getsize(full_path)
            file_metadata[full_path] = size
    return file_metadata

def gettingNLargestFiles(file_metadata,n):
    ''' 
    Shows only the n largest files
    @param file_metadata dictionary
    '''
    items_shown = 0
        
    for path, size in sorted(file_metadata.items(), key=lambda x:x[1], reverse=True):
        if items_shown >= n:
            break
        print(f"Size: {size} Path: {path}")
        items_shown += 1


def main():
    
    file_metadata = traversing(".")
    gettingNLargestFiles(file_metadata,4)
    
if __name__ == "__main__":
    main()