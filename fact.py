#Factorial
import sys,subprocess
import math
while True:
    n=int(input("Enter the number ==> "))
    print("")
    print("The factorial of",n,"is",math.factorial(n))
    print("")
    input("Press any key to continue...")
    subprocess.run("cls",shell=True)
        
