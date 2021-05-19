# Error Handling.

def sum(num1, num2):
    try:
        return num1 + num2

    # except can handle more than one type of error.
    except TypeError as err:
        # to get the error message
        # print("Please enter number", err)
        
        # combining in the string.
        print(f"Please enter the number {err}")
        
        # print error
        # print(err)


print(sum(1, '2'))