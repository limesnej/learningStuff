import math


def calcPi(roundedVal):

    pi = math.pi

    rounded = round(pi, roundedVal)

    return rounded

daInput = int(input("How many digits do you want in your pi? "))

piPieces = calcPi(daInput)

print(f"Here you go: {piPieces}")