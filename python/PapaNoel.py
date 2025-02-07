import random


letters = ["A", "B", "C"]
numbers = ["1", "2", "3"]
password_elements = letters + numbers

def generate_password() -> str:
    return random.sample(password_elements, 4)

secret_password = generate_password()
attemps = 1

while attemps <= 10:
    print(f"Intento: {attemps}")
    
    password = input("Introduce la contraseña: ")

    if len(password) != 4: 
        print("Ërror la contraseña debe de tener cuatro caracteres. ")
        continue
    if not all(character in password_elements for character in password):
        print(f"Solo se permiten los caracteres: {password_elements}")

    if password == secret_password:
        print(f"Contraseña correcta, has acertado en: {attemps} intentos.")
        break
        
    attemps +=1
if attemps > 10:
    print ("Has superado el numero de intentos.")
    print ("Has superado el numero de intentos.")


