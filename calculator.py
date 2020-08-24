def interface():
    print("My Program")
    while True: #Simple way of creating an endless loop
        print("Options for you")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice =='1':
            HDL_driver()
def HDL_driver():
    # Get input
    HDL_result = get_input()
    #Check if HDL is normal
    #Output
def get_input():
    HDL_input = input("Enter your HDL")
    return int(HDL_input)
def Check
interface()
