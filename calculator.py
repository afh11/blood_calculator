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
            return
def HDL_driver():
    # Get input
    HDL_result = get_input()
    #Check if HDL is normal
    Interpretation = check_HDL(HDL_result)
    #Output
    output_HDL(HDL_result, Interpretation)

def get_input():
    HDL_input = input("Enter your HDL: ")
    return int(HDL_input)

def check_HDL(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif 40 <= HDL_result <60:
        return "Borderline Low"
    else:
        return "Low"
def output_HDL(HDL_result, Interpretation):
    print("The HDL result is {}".format(HDL_result))
    print("That is {}".format(Interpretation))
interface()
