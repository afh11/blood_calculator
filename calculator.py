def interface():
    print("My Program")
    while True: #Simple way of creating an endless loop
        print("Options for you")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            return
   
interface()
