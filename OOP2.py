#Funkcja, jako opbiekt pierwszej klasy.
#Funkcje możemy w Pythonie traktować jako wartości

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def apply(fn, a, b):
    return fn(a,b)

oblicz1 = apply(add, 4, 10)
oblicz2 = apply(multiply, 4, 10)

print(oblicz1, " | ", oblicz2)