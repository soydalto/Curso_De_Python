import re

text = "remplazando todas las vocales por asteriscos"

new_text = re.sub("[aeiou]", "*", text)

print(new_text)