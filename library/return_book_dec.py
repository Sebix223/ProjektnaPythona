import os
from datetime import date

def dekorator(func):
    def wrapper(customer_id, book):
        if os.path.exists(f"dataset/{customer_id}.txt"):
            with open(f"dataset/{customer_id}.txt", "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if book in line:
                        lines[i] = line.replace("False", f"{date.today()}")
            with open(f"dataset/{customer_id}.txt", "w") as file:
                file.writelines(lines)
        else:
            print("Książka nie została wypożyczona")
        func(customer_id, book)
    return wrapper