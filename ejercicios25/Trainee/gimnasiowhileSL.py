"""3. Gimnasio “Solo Leveling Fit” - Motivación diaria
Como entrenador, quiero usar un while que repita 5 veces el mensaje “¡Tú puedes lograrlo!”, pero en la última repetición muestre “¡Excelente trabajo, terminaste!”."""

iterador  =  1

while iterador  <  5:
    print ("¡Tu puedes lograrlo!",  iterador)
    if iterador == 4:
        print("¡Excelente trabajo, terminaste!")
        break
    iterador += 1

