# Using type checking you can make variables and functions more bug proof.
num: int = 3
num2: int = 4
def addTwoNumbers(i: int, x: int) -> int:
    print(i + x)
addTwoNumbers(num, num2)

addTwoNumbers("breaks the program", 0.5)