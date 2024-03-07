def print_name_n_times(name,n,cnt=1):
    if cnt>n:
        return
    else: 
        print(name)
    print_name_n_times(name,n,cnt+1)

def main():
    try:
        name = input("Enter the name you want to print: ")
        n = int(input("Print how many you want to print the name: "))    
        if n<1:
            print("Please enter a valid integer.")
            return
        print_name_n_times(name,n)
    except ValueError:
        print("Enter a valid integer")


if __name__=="__main__":
    main()