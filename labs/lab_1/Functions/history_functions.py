from labs.lab_1 import init

if init.history:
    print("\nІсторія обчислень:")
    for record in init.history:
        print(record)