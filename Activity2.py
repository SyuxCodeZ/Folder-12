# input variables

lower = int(input("Enter A Minimum Range: "))

upper = int(input("Enter The Maximum Range: "))

# the loop and conditional statements

for z in range(lower, upper + 1):
    if z > 1:
        for a in range(2, z):
            if (z % a) == 0:
                break

        else:
            print (f"prime numbers are {z}")