"""Escuela “Aprende Más” - Registro de tareas entregadas
Como profesor, quiero usar un while que sume tareas hasta 10. Si el contador llega a 10, mostrar “¡Todas las tareas recibidas!”. Si aún no llega, mostrar cuántas faltan."""

contadortarea = 10
tareas = 0

while tareas < contadortarea:
    print(f"Faltan {contadortarea - tareas} tareas")
    tareas += 1
else:
    print("Todas las tareas recibidas")
    
    
    
    # while iterador  <  5:
    # print ("¡Tu puedes lograrlo!",  iterador)
    # if iterador == 4:
    #     print("¡Excelente trabajo, terminaste!")
    #     break
    # iterador += 1