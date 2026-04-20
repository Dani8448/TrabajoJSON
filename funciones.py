import json
 
 

# Carga del fichero JSON

 
def cargar_datos(ruta: str) -> list:
    """Carga el JSON y devuelve la lista de videojuegos."""
    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f)
    return datos["videojuegos"]
 
 

# 1. LISTAR INFORMACIÓN

 
def listar_videojuegos(videojuegos: list) -> None:
    """Muestra título, año y plataformas de todos los videojuegos."""
    print("\n" + "=" * 65)
    print(f"{'LISTADO COMPLETO DE VIDEOJUEGOS':^65}")
    print("=" * 65)
 
    for i, juego in enumerate(videojuegos, start=1):
        plataformas = ", ".join(juego["plataforma"])
        print(f"\n {i:>2}. {juego['titulo']}")
        print(f"      Año        : {juego['año']}")
        print(f"      Plataformas: {plataformas}")
 
    print("\n" + "=" * 65)



# 2. CONTAR INFORMACIÓN
 
def contar_videojuegos(videojuegos: list) -> None:
    """Muestra el total de videojuegos y cuántos hay por plataforma."""
    print("\n" + "=" * 65)
    print(f"{'CONTEO DE VIDEOJUEGOS':^65}")
    print("=" * 65)
 
    total = len(videojuegos)
    print(f"\n  Total de videojuegos: {total}")
 
    # Conteo por plataforma
    conteo_plataforma: dict = {}
    for juego in videojuegos:
        for plataforma in juego["plataforma"]:
            conteo_plataforma[plataforma] = conteo_plataforma.get(plataforma, 0) + 1
 
    print("\n  Videojuegos por plataforma:")
    print("  " + "-" * 40)
    for plataforma, cantidad in sorted(conteo_plataforma.items()):
        print(f"  {plataforma:<35} {cantidad:>3}")
 
    print("\n" + "=" * 65)
 
 
# 3. FILTRAR POR AÑO

 
def filtrar_por_anio(videojuegos: list, anio_inicio: int, anio_fin: int) -> None:
    """Muestra los videojuegos publicados entre dos años (inclusivo)."""
    print("\n" + "=" * 65)
    print(f"{'VIDEOJUEGOS ENTRE ' + str(anio_inicio) + ' Y ' + str(anio_fin):^65}")
    print("=" * 65)
 
    resultados = [
        j for j in videojuegos if anio_inicio <= j["año"] <= anio_fin
    ]
 
    if not resultados:
        print(f"\n  No se encontraron videojuegos entre {anio_inicio} y {anio_fin}.")
    else:
        for juego in resultados:
            plataformas = ", ".join(juego["plataforma"])
            print(f"\n  • {juego['titulo']} ({juego['año']})")
            print(f"    Plataformas: {plataformas}")
 
    print(f"\n  Total encontrados: {len(resultados)}")
    print("=" * 65)
 
# 4. BUSCAR POR DESARROLLADOR

 
def buscar_por_desarrollador(videojuegos: list, nombre_dev: str) -> None:
    """Muestra todos los videojuegos del desarrollador indicado."""
    print("\n" + "=" * 65)
    print(f"{'VIDEOJUEGOS DE: ' + nombre_dev.upper():^65}")
    print("=" * 65)
 
    resultados = [
        j for j in videojuegos
        if j["desarrollador"]["nombre"].lower() == nombre_dev.strip().lower()
    ]
 
    if not resultados:
        print(f"\n  No se encontraron videojuegos del desarrollador '{nombre_dev}'.")
    else:
        for juego in resultados:
            generos     = ", ".join(juego["genero"])
            plataformas = ", ".join(juego["plataforma"])
            print(f"\n  • {juego['titulo']} ({juego['año']})")
            print(f"    Género(s)   : {generos}")
            print(f"    Plataformas : {plataformas}")
            print(f"    País        : {juego['desarrollador']['pais']}")
 
    print(f"\n  Total encontrados: {len(resultados)}")
    print("=" * 65)
 
 
# 5. EJERCICIO LIBRE – MAYOR PUNTUACIÓN
 
def _media_criticos(juego: dict) -> float:
    """Calcula la media de críticos: (metacritic + ign*10) / 2."""
    metacritic = juego["reseñas"]["criticos"]["metacritic"]
    ign        = juego["reseñas"]["criticos"]["ign"]
    return (metacritic + ign * 10) / 2
 
 
def mostrar_mejor_puntuacion(videojuegos: list) -> None:
    """Muestra el/los videojuego(s) con mayor puntuación media de críticos."""
    print("\n" + "=" * 65)
    print(f"{'VIDEOJUEGO(S) CON MAYOR PUNTUACIÓN DE CRÍTICOS':^65}")
    print("=" * 65)
 
    # Calculamos la media máxima
    puntuacion_max = max(_media_criticos(j) for j in videojuegos)
 
    # Filtramos todos los que tienen esa puntuación máxima
    mejores = [j for j in videojuegos if _media_criticos(j) == puntuacion_max]
 
    print(f"\n  Puntuación máxima de críticos: {puntuacion_max:.2f} / 100")
    print(f"  Número de videojuegos con esa puntuación: {len(mejores)}\n")
    print("  " + "-" * 60)
 
    for juego in mejores:
        generos     = ", ".join(juego["genero"])
        plataformas = ", ".join(juego["plataforma"])
        ventas_tot  = (
            juego["ventas"]["europa"]
            + juego["ventas"]["america"]
            + juego["ventas"]["japon"]
        )
        media       = _media_criticos(juego)
        metacritic  = juego["reseñas"]["criticos"]["metacritic"]
        ign         = juego["reseñas"]["criticos"]["ign"]
 
        print(f"\n   {juego['titulo']}")
        print(f"     Año              : {juego['año']}")
        print(f"     Género(s)        : {generos}")
        print(f"     Plataforma(s)    : {plataformas}")
        print(f"     Desarrollador    : {juego['desarrollador']['nombre']}")
        print(f"     Metacritic       : {metacritic}")
        print(f"     IGN              : {ign:.1f}")
        print(f"     Media críticos   : {media:.2f} / 100")
        print(f"     Ventas totales   : {ventas_tot:.2f} millones")
 
    print("\n" + "=" * 65)





#NUEVAS FUNCIONES

#1.Filtrado por plataforma y genero
    
def filtrado_plat_gen(videojuegos: list, plataforma: str, genero: str) -> None:
    print("FILTRADO POR PLATAFORMA Y GENERO")
    resultados = [
        j for j in videojuegos
        if plataforma in j["plataforma"] and genero.lower() in [g.lower() for g in j["genero"]]
    ]
    if not resultados:
            print("No hay videojuegos de ese género ni plataforma.")
    else:
            for juego in resultados:
                print(f"{juego['titulo']} ({juego['plataforma']})")
    

#2.Calcula la puntuacion minima de todos los juegos

def _media_criticos_min(juego: dict) -> float:
    """Calcula la media de críticos: (metacritic + ign*10) / 2."""
    metacritic = juego["reseñas"]["criticos"]["metacritic"]
    ign        = juego["reseñas"]["criticos"]["ign"]
    return (metacritic + ign * 10) / 2
 
def mostrar_peor_puntuacion(videojuegos: list) -> str:
    """Muestra el/los videojuego(s) con minima puntuación media de críticos."""
    print("\n" + "=" * 65)
    print(f"{'VIDEOJUEGO(S) CON MENOR PUNTUACIÓN DE CRÍTICOS':^65}")
    print("=" * 65)
 
    # Calculamos la media minima
    puntuacion_min = min(_media_criticos_min(j) for j in videojuegos)
 
    # Filtramos todos los que tienen esa puntuación minima
    peores = [j for j in videojuegos if _media_criticos_min(j) == puntuacion_min]
 
    print(f"\n  Puntuación minima de críticos: {puntuacion_min:.2f} / 100")
    print(f"  Número de videojuegos con esa puntuación: {len(peores)}\n")
    print("  " + "-" * 60)
 
    for juego in peores:
        generos     = ", ".join(juego["genero"])
        plataformas = ", ".join(juego["plataforma"])
        ventas_tot  = (
            juego["ventas"]["europa"]
            + juego["ventas"]["america"]
            + juego["ventas"]["japon"]
        )
        media       = _media_criticos(juego)
        metacritic  = juego["reseñas"]["criticos"]["metacritic"]
        ign         = juego["reseñas"]["criticos"]["ign"]
 
        print(f"\n   {juego['titulo']}")
        print(f"     Año              : {juego['año']}")
        print(f"     Género(s)        : {generos}")
        print(f"     Plataforma(s)    : {plataformas}")
        print(f"     Desarrollador    : {juego['desarrollador']['nombre']}")
        print(f"     Metacritic       : {metacritic}")
        print(f"     IGN              : {ign:.1f}")
        print(f"     Media críticos   : {media:.2f} / 100")
        print(f"     Ventas totales   : {ventas_tot:.2f} millones")
 
    print("\n" + "=" * 65)
