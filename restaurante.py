"""Menú: $12.000

Opciones bebida:

sí → $3.000
no → $0
Luego aplicar IVA del 8% al total final.
Mostrar valor con IVA incluido."""
#------------------------------------------------------------------------------

print("RESTAURANTE EL SABOR COLOMBIANO")
print("Menú: $12.000")

menu = 12000
bebida = input("¿Quiere bebida? $3000 (si/no): ").lower()

if bebida == "si":
    total = menu + 3000
    total_final = total * 1.08  
    print("El valor total con bebida:",total_final)
else:    
    total_final = menu * 1.08  
    print("El valor sin bebida es:",total_final)