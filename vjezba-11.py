import random

tajnibroj = random.randint(1,30)

while True:

    pogodi = int(input("Pogodi broj od 1 do 30: "))

    if pogodi == tajnibroj:
        print("Bravo pogodio si traženi broj!")
        break

    else:
        print("Pogriješio si, probaj ponovno.")
