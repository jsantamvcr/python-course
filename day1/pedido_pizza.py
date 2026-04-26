# Descripción:
# Basado en el pedido de un usuario, calcula su factura final. Usa la función input() 
# para obtener las preferencias del usuario, suma el total de su pedido y dile cuánto tiene que pagar.

# Pizza Pequeña (S): $15
# Pizza Mediana (M): $20
# Pizza Grande (L): $25

# Añadir pepperoni para pizza pequeña (Y o N): +$2
# Añadir pepperoni para pizza mediana o grande (Y o N): +$3
# Añadir queso extra para cualquier tamaño de pizza (Y o N): +$1
# Ejemplo de Interacción:

# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M or L: L
# Do you want pepperoni on your pizza? Y or N: Y
# Do you want extra cheese? Y or N: N
# Your final bill is: $28.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")



# todo: work out how much they need to pay based on their size choice.
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
        

# todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is: ${bill}.")

