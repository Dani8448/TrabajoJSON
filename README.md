Este proyecto consiste en un programa en Python que trabaja con un fichero JSON de videojuegos.
El objetivo es poder leer los datos, procesarlos y mostrar información útil a través de un menú.

Estructura del proyecto

proyecto-json-videojuegos/
├── video_games.json
├── main.py
├── funciones.py
├── README.md
└── capturas.pdf

Origen del JSON

El archivo JSON se ha obtenido del proyecto educativo CORGIS y posteriormente se ha modificado para hacerlo más completo.

Fuente: CORGIS
Dataset original: videojuegos
Cambios realizados
Se han convertido géneros y plataformas en listas
Se ha añadido un objeto desarrollador con nombre y país
Se ha añadido un bloque de valoraciones
Se han añadido datos de ventas por regiones
Se ha añadido un sistema de reseñas con críticos y usuarios

Estructura del JSON

El JSON está formado por una lista de videojuegos. Cada uno contiene información como:

Título y año
Géneros y plataformas
Desarrollador
Valoraciones
Ventas
Reseñas

Tiene varios niveles de profundidad (hasta 5), lo que obliga a trabajar bien con diccionarios y listas.

-Funciones principales

Las funciones están en el archivo funciones.py:

cargar_datos(ruta)

Carga el JSON y devuelve los datos.

listar_videojuegos(videojuegos)

Muestra todos los juegos con su año y plataformas.
contar_videojuegos(videojuegos)

Muestra cuántos juegos hay en total y por plataforma.

filtrar_por_anio(videojuegos, inicio, fin)

Filtra juegos dentro de un rango de años.

buscar_por_desarrollador(videojuegos, nombre)

Muestra los juegos de un desarrollador.

_media_criticos(juego)

Calcula la media de críticos.

mostrar_mejor_puntuacion(videojuegos)

Muestra los juegos con mejor puntuación.

pedir_anio(mensaje)

Pide un año y valida que sea correcto.

-Funcionalidades

1. Listar videojuegos

Se muestran todos los videojuegos con:

Título
Año
Plataformas

2. Contar videojuegos

Se muestra:

Total de juegos
Número de juegos por plataforma

3. Filtrar por año

El usuario introduce un rango de años y se muestran los juegos dentro de ese rango.

Si el usuario se equivoca en el orden, el programa lo corrige.

4. Buscar por desarrollador

Permite introducir un desarrollador y ver todos sus juegos.

No distingue entre mayúsculas y minúsculas.

5. Mejor puntuación

Se calcula qué juegos tienen la mejor puntuación de críticos y se muestran junto con sus ventas totales.

-Manejo de errores

Si el fichero no existe → el programa se cierra mostrando error
Si el usuario introduce mal un año → se vuelve a pedir
Si el rango está al revés → se corrige automáticamente

-Ejecución

python main.py

-Dificultades

Trabajar con tantos niveles del JSON fue complicado al principio
Acceder a campos como reseñas (con tilde) daba errores si no se escribía exactamente igual
Calcular la media de críticos requería separar bien la lógica en funciones
-Decisiones

Separar el código en main.py y funciones.py para que sea más claro
Crear una función aparte para la media de críticos
Hacer que el programa sea flexible con los errores del usuario
No limpiar pantalla para poder ver bien los resultados
