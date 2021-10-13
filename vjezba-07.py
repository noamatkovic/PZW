import random

x = random.randint(1,10)

# print(x)

a = int(input("Pogodi broj od 1 do 10: "))

if x == a:
    print("Bravo, pogodio si traženi broj.")
else:
    print("Netočno, traženi broj je bio {0}.".format(x))

