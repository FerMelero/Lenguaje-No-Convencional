## Instrucciones:

* **jmp** → salto incondicional (jmp skip)
* **tag** (etiqueta - no es una instrucción, con él nuestro ensamblador sabrá en dónde estará una función) (tag skip)
* **jeq** / **jne** (jump if equal) / (jump if not equal) (jeq $t9, 1, true_tag) (tiene que estar definida la etiqueta)
* **slt** (set lower than) "<" (slt $t9, $t3, 35)
* **sgt** (set greater than) ">" (sgt $t9, $t3, 35)
* **svc** —> svc1 (salir) svc2 (print) (Llamadas al sistema (service call)) (svc2 $t2)
* **mov** (mover valor de un lado a otro) (mov $t3, $t10)



## Registros:

ㅤ  ↓ Registros para los tréboles (del 2 al 10)<br>
<strong>aux 2 3 4 5 6 7 8 9 10 </strong>                   
↑↓ Registros auxiliares <br>
**result** <!--(otra variable auxiliar para cuando llamemos a una función guardar el valor de retorno) -->


## Arquitectura:

<img width="1378" height="566" alt="image" src="https://github.com/user-attachments/assets/78124284-82d0-44ff-a736-40e3b9671fb1" />

