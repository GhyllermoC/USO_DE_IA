# Uso de Inteligencia Artificial en este Proyecto

## Herramientas utilizadas
- Microsoft (Copilot) / para generación de funciones.

## Detalle: [IA_USAGE/codigo.py]
- **Prompt utilizado:** "Actúa como un programador. Genera una función llamada validar_numero (numero telefonico) que verifique si el texto ingresado tiene 10 dígitos numéricos y cumple con la condicion que empiece con 09. Devuelve True si es válida o False si no. Dame únicamente el código limpio, sin explicaciones, sin comentarios y sin manejo de errores. Todo esto en Python 3.11."
- **Código Inicial de IA:** [def validar_numero(numero_telefonico: str) -> bool:
    return len(numero_telefonico) == 10 and numero_telefonico.isdigit() and numero_telefonico.startswith("09")]
- **Cambios realizados**
  1. Implementacion de 4 excepciones con el fin de atrapar posibles errores que se presenten durante el ingreso de datos por parte del usuario y de igual manera poder brindar una mejor experiencia.
## Política: todo código asistido por IA debe ser comprendido, probado y documentado.
