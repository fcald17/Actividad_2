# Juego de la Víbora en Python 
El clásico juego de la víbora, pero usando la interface visual de Python. El código original fue obtenido del sitio Grant Jenks y dentro de este repositorio se encuentra el programa del juego con diferentes cambios realizados por el equipo.

## Acerca del Código Base y su Funcionamiento
El juego es bastante simple, la serpiente debe de comer los alimentos que van apareciendo en pantalla para poder crecer. El usuario puede mover a la serpiente utilizando las flechas del teclado, pero si choca con el límite de la pantalla o con su propio cuerpo, su cabeza se torna roja y el juego se acaba.

## Cambios Realizados al Código Base
Para volver el juego más difícil y atractivo visualmente, dentro de este repositorio se hicieron dos cambios al código original.
### Primer Cambio: Colores Aleatorios
Se creó una lista de cinco colores diferentes al rojo, que es el color de derrota, para colorear el cuerpo de la serpiente y la comida. Estos se eligen al azar y siempre son diferentes uno del otro. Se cambian cada vez que se reinicia el juego
### Segundo Cambio: Comida Aleatoria
Para volverlo más complicado, decidimos que, si la comida no se consume en una cierta cantidad de tiempo, esta cambie de posición a un nuevo lugar esogido de manera aleatoria aumentando en su dificultad.|:
