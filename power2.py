n = int(input("Enter your number: "))
def checkIfPowerof2(n):
    if(n<=0):
        return False
    if(n==1):
        return True
    if(n%2==0):
        return checkIfPowerof2(n/2)
    return False
if(checkIfPowerof2(n)):
    print("Power of 2")
else:
    print("Not a power of 2")