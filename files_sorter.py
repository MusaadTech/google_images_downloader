import os


# Function to rename multiple files
def main():
    i = 0
    path = "C:\\datasets\\Saudi_Plates\\bing\\7\\"
    files = os.listdir(path)
    files.sort()
    my_dest = ''
    my_source = ''
    for filename in files:
        try:
            my_dest = path + str(i + 1) + f'.{filename.split(".")[1]}'
            my_source = path + filename
        except:
            my_dest = path + str(i + 1)
            my_source = path + filename
        # rename() function will
        # rename all the files
        os.rename(my_source, my_dest)
        i += 1


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
