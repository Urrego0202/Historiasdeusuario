"""El usuario ingresa dos notas (0.0 - 5.0):

Prueba técnica (70%)
Prueba lógica (30%)
Cálculo: nota_final = (tecnica * 0.7) + (logica * 0.3)

Condiciones:

nota_final ≥ 3 → “Aprobado”
2 ≤ nota_final < 3 → “Revisión”
< 2 → “Reprobado”
Validar que las notas estén en rango."""
#-----------------------------------------------------------------
print("EMPRESA TECNOPLUS")

resultadotecnica = float(input("Ingresa nota de prueba técnica (0.0 / 5.0): "))
resultadologica = float(input("Ingresa nota de prueba lógica (0.0 / 5.0): "))

nota_final = (resultadotecnica * 0.7) + (resultadologica * 0.3)
if 0.0 <= resultadotecnica <= 5.0 and 0.0 <= resultadologica <= 5.0:
    if nota_final >= 3:
        print("Aprobado", nota_final)
    elif 2 <= nota_final < 3:
        print("Revisión",nota_final)
    elif nota_final < 2:
        print("Reprobado",nota_final)
else:
    print("La nota no está en el rango")