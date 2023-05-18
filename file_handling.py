def file_handling():
    choice = input("Press 1 for show the files: \nPress 2 for write a file: ")
    if choice=="1":
        file_read()
    elif choice=="2":
        file_writing()
        
def file_writing():
    try:
        file = input("Enter the filename you want to write: ")
        f = open(file,"x")
        choice = input("do you want to write the {} file? [y]/[n]".format(file))
        if choice == "y":
            print("Start writing")
            data = input("")
            f.write(data)
            f.close()
            print("-----------------------------------------")
            read = input("Do you want show the {} file? [y]/[n]".format(file))
            if read=="y":
                f = open(read,"r")
                print(f.read())
                f.close()
                print("-----------------------------------------")
            if read=="n":
                f.close()
                print("-----------------------------------------")
                file_handling()
        else:
            f.close()
            print("-----------------------------------------")
            file_handling()
            
    except:
        raise Exception("File is already exist")
    
def file_read():
    try:
        read_file = input("Enter the file_name you want to read")
        f = open(read_file,"r")
        print(f.read())
        f.close()
        print("-----------------------------------------")
        file_handling()
    except:
        raise Exception("File name mismatched")

file_handling()
print("good")
    
