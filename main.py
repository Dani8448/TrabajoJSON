from funciones import (
    cargar_datos,
    listar_videojuegos,
    contar_videojuegos,
    filtrar_por_anio,
    buscar_por_desarrollador,
    mostrar_mejor_puntuacion,
    filtrado_plat_gen,
    mostrar_peor_puntuacion
)
 
RUTA_JSON = "video_games.json"
 
def mostrar_menu() -> None:
    print("\n" + "╔" + "═" * 55 + "╗")
    print("║" + " MENÚ PRINCIPAL – VIDEOJUEGOS ".center(55) + "║")
    print("╠" + "═" * 55 + "╣")
    print("║  1. Listar todos los videojuegos                      ║")
    print("║  2. Contar videojuegos (total y por plataforma)       ║")
    print("║  3. Filtrar por rango de años                         ║")
    print("║  4. Buscar por desarrollador                          ║")
    print("║  5. Videojuego(s) con mayor puntuación de críticos    ║")
    print("║  6. Videojuego(s) filtrados por plataforma y genero   ║")
    print("║  7. Videojuego(s) con menor puntuación de críticos    ║")
    print("║  0. Salir                                             ║")
    print("╚" + "═" * 55 + "╝")
 
def pedir_anio(mensaje: str) -> int:
    pedir = 1
    while pedir == 1:
        valor = input(mensaje).strip()
        if valor.lstrip("-").isdigit():
            return int(valor)
        print("  ⚠  Por favor, introduce un número entero válido.")
 
def main() -> None:
    print("\n  Cargando datos desde:", RUTA_JSON)
    try:
        videojuegos = cargar_datos(RUTA_JSON)
        print(f"  ✔ {len(videojuegos)} videojuegos cargados correctamente.")
    except FileNotFoundError:
        print(f"  ✘ Error: no se encontró el fichero '{RUTA_JSON}'.")
        print("    Asegúrate de que el JSON está en la misma carpeta que main.py.")
        return
 
    ejecutando = 1
    while ejecutando == 1:
        mostrar_menu()
        opcion = input("\n  Selecciona una opción: ").strip()
 
        if opcion == "1":
            listar_videojuegos(videojuegos)
        elif opcion == "2":
            contar_videojuegos(videojuegos)
        elif opcion == "3":
            print("\n  -- Filtrar por rango de años --")
            anio_inicio = pedir_anio("  Año inicial : ")
            anio_fin    = pedir_anio("  Año final   : ")
            if anio_inicio > anio_fin:
                anio_inicio, anio_fin = anio_fin, anio_inicio
            filtrar_por_anio(videojuegos, anio_inicio, anio_fin)
        elif opcion == "4":
            print("\n  -- Buscar por desarrollador --")
            nombre = input("  Nombre del desarrollador: ").strip()
            if nombre:
                buscar_por_desarrollador(videojuegos, nombre)
            else:
                print(" No has introducido ningún nombre.")
        elif opcion == "5":
            mostrar_mejor_puntuacion(videojuegos)
        elif opcion == "6":
            plataforma = input('Introduzca la plataforma: ')
            genero = input('Introduzca el genero: ')
            filtrado_plat_gen(videojuegos, plataforma, genero)
        elif opcion == "7":
            mostrar_peor_puntuacion(videojuegos)
        elif opcion == "0":
            print("\n  ¡Hasta luego!\n")
            ejecutando = 0
        else:
            print("\n Opción no válida. Elige un número del 0 al 5.")
 
        if ejecutando == 1:
            input("\n  Pulsa ENTER para continuar...")
 
if __name__ == "__main__":
    main()
