# _author_Adrian Fernandez
# Project Zeus
# Includes Python facts as well


def main():
    for _ in range(2):

        print("0.Creator ", " Program Info", sep='&')
        print("Welcome to ", end='')
        print("Project Zeus")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponents")
        print("6. Guessing game")
        print("7. Python Q and A")
        print("8. Python game")
        print("9. Motivational quote")

        x = int(input("Enter a number: "))

        while x < 0 or x > 9:
            print("Choose a number between 0 and 9")
            x = int(input("Enter a number: "))

        print(
            "-------------------------------" * 6)  # creates a border after you pick a number

        if x == 1:

            a = int(input("enter first number."))
            b = int(input("enter second number."))
            a += b  # adding the two numbers you input
            print("Sum: ", a)

        elif x == 0:

            my_function("Adrian")

        elif x == 2:

            a = int(input("enter first number."))
            b = int(input("enter second number."))
            subtract = a - b  # subtracting the two numbers you input
            print("Subtract: ", subtract)

        elif x == 3:

            a = int(input("enter first number."))
            b = int(input("enter second number."))
            Multiply = a * b  # multiplying the two numbers you input
            print("Multiply: ", Multiply)

        elif x == 4:

            a = int(input("enter first number."))
            b = int(input("enter second number."))
            Divide = a / b  # diving the two numbers you input
            print("Divide: ", Divide)

        elif x == 5:

            a = int(input("enter first number."))
            b = int(input("enter exponent."))
            Exponent = a ** b  # making b the exponent of the first number
            # then solving the equation
            print("Exponent:", Exponent)

        elif x == 6:

            computer_num = 3
            a = int(input("Enter between 1 - 5"))
            if computer_num != a:
                if computer_num > a:
                    print("Your number is less than computer")
            else:
                print(not computer_num)

        elif x == 7:

            correct = 1

            a = int(input("Is this program writen in python? Enter 1 for True "
                          "or 0 for False: "))
            b = int(
                input("Did Guido van Rossum create Python? Enter 1 for True"
                      " or 0 for False: "))
            if a == correct and b == correct:
                print("You won Python Q and A!")
            else:
                print("NOPE!")

        elif x == 8:

            int(input("Was Python created in 1991? Enter 1 for True or 0 "
                      "for False:  "))
            x = ["1991"]
            print("1991" in x)

        elif x == 9:

            a = int(input("Select between 1 - 5 = "))

            if a == 1:

                print("The road to success and the road to failure are almost"
                      "exactly the same. — Colin R. Davis \n")

            elif a == 2:
                print("Don’t let yesterday take up too much of today — Will"
                      "Rogers \n")

            elif a == 3:
                print("“Your work is going to fill a large part of your "
                      "life,\n"
                      " and the only way to be truly satisfied is to do "
                      "what \n"
                      "you believe is great work. And the only way to do "
                      "great \n"
                      "work is to love what you do. If you haven't found "
                      "it \n"
                      " yet, keep looking. Don't settle. As with all "
                      "matters \n"
                      "of the heart, you'll know when you find it.” — Steve J"
                      "obs \n")

            elif a == 4:
                print("“Don't settle for average. Bring your best to the "
                      "moment. \n"
                      "Then, whether it fails or succeeds, at least you know"
                      "\n"
                      "you gave all you had.” —Angela Bassett \n")

            elif a == 5:
                print("Nothing in the world can take the place of "
                      "Persistence. \n"
                      "Talent will not; nothing is more common than \n"
                      "unsuccessful men with talent. Genius will not; \n"
                      "unrewarded "
                      "genius is almost a proverb. Education will not; the \n"
                      "world is full of educated derelicts. The slogan\n "
                      "'Press "
                      "On' has solved and always will solve the problems of "
                      "the human race. —Calvin Coolidge \n")


def my_function(name=""):
    print(name + " Fernandez")  # (+) string operator is adding Fernandez to
    # Adrian
    print("This program works as a calculator to solve any basic equation")


main()
