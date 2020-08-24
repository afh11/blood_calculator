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
   
interface()
