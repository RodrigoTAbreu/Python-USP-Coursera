def vogal(x):
    vogais = ('a','A','e','E','i','I','O','o','U','u')
    # x = input("vogal:")
    if x in vogais:
        return True
    else:
        return False

print(vogal("i"))