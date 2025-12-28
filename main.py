def main():
    try:
        firstNumber = int(input('Enter your number:'))
    except ValueError:
        print("Not a number")
        return
    try:
        secondNumber = int(input('Enter your number:'))
    except ValueError:
        print("Not a number")
        return
    
    symbol = input("Enter your symbol:")
    
    if symbol == '+':
        return print(firstNumber + secondNumber)
    if symbol == '-':
        return print(firstNumber - secondNumber)
    if symbol == '*':
        return print(firstNumber * secondNumber)
    if symbol == '/':
        return print(firstNumber / secondNumber)
    
main()