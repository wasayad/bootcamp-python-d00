import sys

error = 0
if len(sys.argv) is not 3:
    print("Inputerror: too many arguements\n")
    print("Usage: puthon operations.py <number1> <number2>")
    print("Example:\n")
    print("    python operations.py 10 3")
    exit()
sys.argv.remove(sys.argv[0])
for i in range(0,len(sys.argv[0])):
    if sys.argv[0][i].isdigit() is not True and (sys.argv[0][i] is not '-' or i is not 0):
        print("Inputerror: only numbers")
        print("Usage: puthon operations.py <number1> <number2>")
        print("Example:\n")
        print("    python operations.py 10 3")
        exit()
for i in range(0,len(sys.argv[1])):
    if sys.argv[1][i].isdigit() is not True and (sys.argv[1][i] is not '-' or i is not 0):
        print("Inputerror: only numbers")
        print("Usage: puthon operations.py <number1> <number2>")
        print("Example:\n")
        print("    python operations.py 10 3")
        exit()
a = int(sys.argv[0])
b = int(sys.argv[1])
print("Sum:          ", a + b)
print("Difference:   ", a - b)
print("Product:      ", a * b)
if b is not 0:
    print("Quotient:     ", a / b)
else:
    print("Quotient:      ERROR (div by zero)")
    error = 1
if b is not 0:
    print("Quotient:     ", a % b)
else:
    print("Quotient:      ERROR (modulo by zero)")
    error = 1
if error is 1:
    print("\nUsage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")