from labs.lab_2 import init

if init.history:
    print("\nІсторія обчислень:")
    for record in init.history:
        print(record)