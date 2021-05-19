while True:
    try:
        age = int(input("What is your age? "))
        10/age
    except ValueError:
        print("Please enter a number")
        continue
    except ZeroDivisionError:
        print("Please enter number higher than 0")
        break
    else:
        print("thank you!!!")
        break
    finally:
        print('okay, i am finally done')
    print('can you hear me?')