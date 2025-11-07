"""3. Gimnasio “Solo Leveling Fit” — Motivación + Bono
Pedir cuántos días entrenó esta semana.

≥ 4 días → "¡Excelente disciplina!" + gana 1 punto de energía
2 o 3 → "Bien, pero puedes dar más"
0 o 1 → "No aflojes, tú puedes mejorar"
Mostrar mensaje y si aplica, los puntos ganados."""

print("GIMNASIO SOLO LEVELING")

diasentrenados = int(input("Ingresa los días entrenados: "))
puntosdeenergia = 0

if diasentrenados >= 4:
    print("¡Excelente disciplina!")
    puntosdeenergia = 1
elif diasentrenados >= 2:
    print("Bien, pero puedes dar más")
else:
    print("No aflojes, tú puedes mejorar")

if puntosdeenergia > 0:
    print("Has ganado", puntosdeenergia, "punto de energía")
else:
    print("No has ganado puntos de energía")
