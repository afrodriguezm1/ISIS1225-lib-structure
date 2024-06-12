import os


def print_test_options():
    print("Bienvenido a las pruebas unitarias de DISCLib")
    print("1. Todas las estructuras")
    print("2. Lista")
    print("3. Árbol")
    print("4. Grafo")
    print("0. Salir")


def execute_all_tests():
    execute_list_tests()


def execute_list_tests():
    os.system('pytest -v -k "test_array_list"')
    os.system('pytest -v -k "test_linked_list"')
    # os.system('pytest -v -k "test_double_linked_list"')


if __name__ == "__main__":
    """
    Menu principal de pruebas unitarias
    """
    running = True
    while running:
        print_test_options()
        input_option = input(
            "Ingrese el número de la opción que desea ejecutar: \n")
        if int(input_option) == 1:
            os.system('pytest -v')
        if int(input_option) == 2:
            execute_list_tests()
        if int(input_option) == 0:
            running = False
            print("Saliendo de las pruebas unitarias")
        else:
            print("Opción no válida")

        repeat = input("Desea ejecutar otra prueba? (1. Si 2. No)\n")
        if int(repeat) == 2:
            running = False
            print("Saliendo de las pruebas unitarias")
