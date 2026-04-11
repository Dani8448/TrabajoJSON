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