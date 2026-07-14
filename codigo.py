## Codifo generado por la IA.
def validar_numero(numero_telefonico: str) -> bool:
    return len(numero_telefonico) == 10 and numero_telefonico.isdigit() and numero_telefonico.startswith("09")

## Codigo corregido manualmente.  
## Si bien es un codigo generado por la IA es ideal para lo que se esta buscando,
## que es la validacion de numeros telefonicos. Realizare la implementacion de
## varias condiciones con el fin de mejorar la interaccion con el usuario.
def validar_numero(numero_telefonico):
      
    numero_telefonico= numero_telefonico.strip()
    if len(numero_telefonico) == 10 and numero_telefonico.isdigit() and numero_telefonico.startswith("09"):
        return True
        
    elif numero_telefonico == "":
        return "Campo obligatorio. Ingrese su numero telefonico"
    
    elif not numero_telefonico .isdigit():
        return "Ingrese solo numeros"

    elif len(numero_telefonico) != 10:
        return "Su numero telefonico debe contener 10 numeros"
        
    elif not numero_telefonico.startswith("09"):
        return "Su numero debe comenzar con 09"  
    


## PROGAMA 
##No es lo ideal en cuestion de buena practica de programacion
##Servira para el fin.

print("SISTEMA DE VALIDACION DE NUMEROS TELEFONICOS")

while True:
    numero_telefonico = input("Ingresa tu numero de telefono: ")
    resultado= validar_numero(numero_telefonico)
    if resultado == True:
        print("Correcto. Guardando numero telefonico...")
        break
    else:
        print (resultado)

print("Gracias por usar este sitema de validacion de numeros")
