def calcular():

    operação = input ('''
Please enter the math operation you'd like to complete
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    num1 = int (input ("Enter your first number: "))
    num2 = int (input ("Enter your second number: "))

#print (num1 + num2)

    if operação == "+":
#Adição
        print("{} + {} =".format(num1, num2))
        print(num1 + num2)

    elif operação == "-":
#Subtração
        print("{} - {} =".format(num1, num2))
        print(num1 - num2)

    elif operação == "*":
#Multiplicação
        print("{} * {} = ".format(num1, num2))
        print(num1 * num2)

    elif operação == "/":
#Divisão
        print("{} / {} = ".format(num1, num2))
        print(num1 / num2)
    else:
        print("You have not typed a valid operator, please run the program again.")
    again ()
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calcular()
    elif calc_again.upper() == 'N':
        print('See you later. Type exit and press enter to finish the program')
    else:
        again()
calcular()