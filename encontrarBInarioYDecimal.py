import random

print (" \n🚀 Bienvenido al programa de adivinanza binaria y decimal")

numero_decimal = random.randint(1, 100)  
numero_binario = bin(numero_decimal)[2:]  

intentos = 0  
intentos_maximos = 3  

while intentos < intentos_maximos:
     respuesta_usuario = input(f"Intenta adivinar el número decimal (entre 1 y 100) de {numero_binario}: ")

     if respuesta_usuario.isdigit() and int(respuesta_usuario) == numero_decimal:
         print("¡Felicidades! Has adivinado el número decimal correctamente. Pasaste al siguiente nivel 🎉")
     else:
           intentos += 1
           print(f"Intenta de nuevo. Te quedan {intentos_maximos - intentos} intentos.")

if intentos == intentos_maximos:
     print(f"Lo siento, has agotado tus intentos. El número decimal era {numero_decimal}.")
     print("Fin del juego. Gracias por jugar.")
else:
     print("\n🔷 Nivel 2: Ahora convierte un número decimal a binario!")
     numero_decimal_2 = random.randint(1, 100) 
     numero_binario_2 = bin(numero_decimal_2)[2:]

     respuesta_usuario_2 = input(f"¿Cuál es el número binario de {numero_decimal_2}? (Escribe el número binario sin ceros a la izquierda) ")

     if respuesta_usuario_2 == numero_binario_2:
           print("¡Felicidades! Has adivinado el número binario correctamente. 🎉"
                 " Fin del juego. Gracias por jugar.")
     else:
               print(f"Lo siento, la respuesta correcta era {numero_binario_2}. Fin del juego. Gracias por jugar.")