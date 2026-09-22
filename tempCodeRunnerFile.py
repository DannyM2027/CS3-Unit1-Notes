#careful with int list , str

    # int x= 5, floats: x = 500.1, complex: x = 30j

    grade = 92.87
    print("your grade is:")
    print(int(grade))

    # int/int = float, int + float = float
    x = 5
    x = float(x)
    print(type(x)) # declared
    print(x)

    # quotes for strings (single apostrophes)
    # triple quotes
    print("""helo""")
    class_size = 5

    print('hello class of ' + str(class_size) +'!')


    # printing w fStrings
    print(f"helo class of {class_size}!")

    matthew_age = 1
    print(f"matthew is {matthew_age} years old!")
        
    number = "5.0"
    number = int(float(number))
    print(type(number))
    print(f"our out put is {number}")
    name_of_function()