Proyecto: Gestión de Videojuegos con JSON en Python
Descripción

Este proyecto consiste en un programa en Python que trabaja con un fichero JSON de videojuegos.
El objetivo es leer los datos, procesarlos y mostrar información útil mediante un menú interactivo.

Estructura del proyecto
proyecto-json-videojuegos/
│
├── video_games.json
├── main.py
├── funciones.py
├── README.md
└── capturas.pdf
Origen del JSON

El archivo JSON proviene del proyecto educativo CORGIS y ha sido modificado para enriquecer los datos.

Fuente original
Dataset CORGIS: videojuegos
Cambios realizados
Conversión de géneros y plataformas en listas
Añadido un objeto "desarrollador" con nombre y país
Incorporación de un bloque de valoraciones
Inclusión de ventas por regiones
Sistema de reseñas con críticos y usuarios
Estructura del JSON

El archivo contiene una lista de videojuegos. Cada videojuego incluye:

Título y año
Géneros y plataformas
Desarrollador
Valoraciones
Ventas
Reseñas

Nota:
La estructura tiene hasta 5 niveles de profundidad, lo que requiere un buen manejo de diccionarios y listas en Python.

Funciones principales (funciones.py)
Carga de datos
cargar_datos(ruta)
Carga el JSON y devuelve los datos.
Visualización
listar_videojuegos(videojuegos)
Muestra todos los juegos con su año y plataformas.
contar_videojuegos(videojuegos)
Muestra el total de juegos y el número por plataforma.
Filtros y búsqueda
filtrar_por_anio(videojuegos, inicio, fin)
Filtra juegos dentro de un rango de años.
buscar_por_desarrollador(videojuegos, nombre)
Busca juegos por desarrollador (sin distinguir mayúsculas/minúsculas).
Cálculos
_media_criticos(juego)
Calcula la media de puntuaciones de críticos.
mostrar_mejor_puntuacion(videojuegos)
Muestra los juegos con mejor puntuación junto con sus ventas.
Entrada de datos
pedir_anio(mensaje)
Solicita un año y valida la entrada del usuario.
Funcionalidades del programa
Listar videojuegos

Se muestran:

Título
Año
Plataformas
Contar videojuegos

Se muestra:

Número total de juegos
Número de juegos por plataforma
Filtrar por año
El usuario introduce un rango de años
Si el orden es incorrecto, el programa lo corrige automáticamente
Buscar por desarrollador
Permite introducir el nombre de un desarrollador
No distingue entre mayúsculas y minúsculas
Mejor puntuación
Calcula qué juegos tienen la mejor puntuación de críticos
Muestra también sus ventas totales
Manejo de errores
Si el fichero no existe: el programa se cierra mostrando un error
Si el usuario introduce un año incorrecto: se vuelve a pedir
Si el rango de años está invertido: se corrige automáticamente
Ejecución
python main.py
Dificultades encontradas
Manejar múltiples niveles del JSON
Acceder correctamente a claves con caracteres especiales (como "reseñas")
Separar la lógica para calcular la media de críticos
Decisiones de diseño
Separación del código en main.py y funciones.py para mayor claridad
Creación de funciones específicas para tareas concretas
Manejo flexible de errores del usuario
No limpiar la pantalla para facilitar la visualización de resultados
