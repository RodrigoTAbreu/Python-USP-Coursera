def fizzbuzz(numero):
    #numero = int(input("Informe um valor: "))

    if numero % 3 == 0 and not numero % 5 == 0:
        return "Fizz"
    elif numero % 5 == 0 and not numero % 3 == 0:
        return "Buzz"
    elif numero % 5 == 0 and numero % 3 == 0:
        return "FizzBuzz"
    elif numero % 5 !=0 and numero % 3 !=0:
        return numero

print(fizzbuzz(3))