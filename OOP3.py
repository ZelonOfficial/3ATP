#DEKORATORY W PYTHONIE
#dekoratory zmieniają zachowanie funkcji
#dekoratory są to inne funkcje
#Robimy to po to, zby zrobić rózne warianty funkcji
#dekorator pozwoli nam wpłynąć na dynamiczne zachowanie funkcji

def my_decorator(fn):
    def wrapper():
        print("Początkowe obliczanie")
        fn()
        print("Koniec odiczania")
    return wrapper


def get_5_values():
    for v in range(1,6):
        print(v)

get_5_values()
get_5_values_decorstor = my_decorator(get_5_values)
get_5_values_decorstor()