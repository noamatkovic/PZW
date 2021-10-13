a = int(input("Unesi a: "))

b = int(input("Unesi b: "))

suma = a + b 

razlika = a - b

količnik = a / b 

umnožak = a * b

c = input("Unesi matematičku operaciju: ")

if c == "+":
    print(suma)
elif c == "-":
    print(količnik)
elif c == "*":
    print(umnožak)
elif c == "/":
    print(količnik)
else: 
    print("Netočno uneseno.")
    