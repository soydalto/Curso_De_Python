import re

email = "lucasdaltonuevogmail@gmail.c"

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.match(pattern, email)

if result:
    print("Dirección de correo válida")
else:
    print("Dirección de correo inválida")