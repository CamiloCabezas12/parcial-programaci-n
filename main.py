#CAMILO ANDRES CABEZAS CRUZ
#ID 1023048

from pelicula import Pelicula

def main():
    #3 obejtos(peliculas)
    pelicula1 = Pelicula(1, "Rápidos y Furiosos 5", 130, "Justin Lin", False)
    pelicula2 = Pelicula(2, "Pena Máxima", 122, "Taylor Hackford", True)
    pelicula3 = Pelicula(3, "Cars", 117, "John Lasseter", False)

    #informacion
    print("=== INFORMACIÓN DE PELÍCULAS ===")
    print(pelicula1)
    print(pelicula2)
    print(pelicula3)

    #metodos
    print("\n=== PRESTAR Y DEVOLVER ===")
    pelicula1.prestar()
    pelicula2.prestar()
    pelicula2.devolver()
    pelicula3.devolver()

    #costo
    tarifa = 0.25
    print("\n=== COSTOS DE REPRODUCCIÓN ===")
    print(f"{pelicula1.titulo}: ${pelicula1.costo_reproduccion(tarifa):.2f}")
    print(f"{pelicula2.titulo}: ${pelicula2.costo_reproduccion(tarifa):.2f}")
    print(f"{pelicula3.titulo}: ${pelicula3.costo_reproduccion(tarifa):.2f}")

    #comparación
    print("\n=== COMPARACIÓN ===")
    print(f"¿Película 1 == Película 2? {pelicula1 == pelicula2}")  
    print(f"¿Película 1 == Película 3? {pelicula1 == pelicula3}")  
    print(f"¿Película 2 == Película 3? {pelicula2 == pelicula3}") 

if __name__ == "__main__":
    main()