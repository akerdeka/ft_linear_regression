import sys

try:
    mileage = int(input("Enter a mileage: "))
except ValueError:
    print("Oops!  That was no valid number.")
    exit(1)

try:
    file = open("data.txt", 'r')
    data = file.read().split(" ")
    print(data)
    theta0 = float(data[0])
    theta1 = float(data[1])
    file.close()
except:
    theta0 = 0
    theta1 = 0

print("Prix éstimé : {0}".format(theta0 + (theta1 * int(mileage))))