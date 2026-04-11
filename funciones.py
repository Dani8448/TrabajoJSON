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
 
 