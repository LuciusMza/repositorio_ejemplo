#Para crear un archivo con git se debe empezar creando el repositorio con git init

# Después se configura el archivo y se pone git add nombre_archivo.py o nombre_carpeta/, para que el repositorio quede en la zona 
# de transición ()

# Por último, para que el cambio quede definido de forma permanente tenemos que poner git commit -m "y acá va un mensaje/comentario"

# git log se usa para mostrar cuáles fueron los cambios y quién los hizo

# git status muestra cuál es el estado de los archivos modificados (si están agregados o en transición)

# Ramas: se usa el comando git branch para mostrar cuáles ramas se han creado y el comando git branch nombre_rama para crear una rama nueva
# Para trasladarnos a esa rama nueva tenemos que usar el comando git checkout nombre_rama y listo
# Ahora bien, si nosotros nos cambiamos de una rama a otra sin fusionar las ramas, en la rama original (master) los 
# cambios no van a estar guardados. Pero si volvemos a la nueva rama, los cambios van a seguir ahí 