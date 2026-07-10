def validar_numero(numero_telefonico: str) -> bool:
    return len(numero_telefonico) == 10 and numero_telefonico.isdigit() and numero_telefonico.startswith("09")
