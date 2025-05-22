#CAMILO ANDRES CABEZAS CRUZ
#ID 1023048
class Pelicula:
    def __init__(self, codigo=0, titulo="", duracion=0, director="", prestada=False):
        self._codigo = codigo
        self._titulo = titulo
        self._duracion = duracion
        self._director = director
        self._prestada = prestada

    #getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def titulo(self):
        return self._titulo

    @property
    def duracion(self):
        return self._duracion

    @property
    def director(self):
        return self._director

    @property
    def prestada(self):
        return self._prestada

    #setters
    @codigo.setter
    def codigo(self, nuevo_codigo):
        self._codigo = nuevo_codigo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    @duracion.setter
    def duracion(self, nueva_duracion):
        self._duracion = nueva_duracion

    @director.setter
    def director(self, nuevo_director):
        self._director = nuevo_director

    @prestada.setter
    def prestada(self, nuevo_estado):
        self._prestada = nuevo_estado

    #métodos
    def prestar(self):
        if not self._prestada:
            self._prestada = True
        else:
            print(f"{self._titulo} ya está prestada")

    def devolver(self):
        if self._prestada:
            self._prestada = False
        else:
            print(f"{self._titulo} no estaba prestada")

    def costo_reproduccion(self, tarifa_por_minuto):
        return self._duracion * tarifa_por_minuto

    def __str__(self):
        estado = "está" if self._prestada else "no está"
        return f'La película {self._codigo} titulada "{self._titulo}" dirigida por {self._director} dura {self._duracion} minutos y {estado} prestada.'

    def __eq__(self, otra):
        return self._codigo == otra.codigo